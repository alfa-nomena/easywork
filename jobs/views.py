from django.shortcuts import render
from .models import Job
from faker import Faker
from django.contrib.auth.models import User
import numpy as np
from django.utils import timezone
from users.models import Candidate
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import SearchForm


class ListAllJobsView(ListView):
    model=Job
    paginate_by=50
    template_name = 'jobs/list-all-jobs.html'
    context_object_name='jobs'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (kwargs.get('request')) and (kwargs.get('request').method=='POST'):
            request = kwargs.get('request').POST
            filters = {}
            key_word = request.POST.get('key_word')
            experience = request.POST.get('experience')
            category = request.POST.get('category')
            
            if key_word!='':
                filters['title']=key_word
            if experience!='':
                filters['experiences']=experience
            if category!='':
                filters['job_type']=category
            jobs = Job.objects.filter(**filters)
            if len(jobs)>20:
                jobs = jobs[:20]
            context['jobs']=jobs
        return context
    

class DetailJobView(DetailView):
    model = Job
    template_name = 'jobs/detail-job.html'
    


def home(request):
    jobs = Job.objects.all()
    if len(jobs)<5:
        _create_fake_data()
        jobs = Job.objects.all()
    context = {
        "jobs":jobs[:20],
        'job_experiences':dict(Job.EXPERIENCES),
        'job_categories':dict(Job.TYPES),
    }
    user = request.user
    if user.is_authenticated:
        if candidate := Candidate.objects.filter(user=user):
            context['candidate'] = candidate[0]
    template = 'jobs/index.html'
    context["search_form"]= SearchForm()
    return render(request, template, context)

def _create_fake_user():
    faker = Faker()
    user = User.objects.create_user(
        username='test', 
        password='test', 
        first_name = faker.first_name(),
        last_name = faker.last_name(),
        email=faker.email(),
        is_superuser=True,
        is_staff=True,
    )
    # user.is_superuser = True
    # user.is_staff = True
    user.save()
    candidate = Candidate(
        user=user,
        sex="M", 
        birth=faker.date(),
        title=faker.text(100),
        description = faker.text(1000), 
        facebook = faker.name(),
        twitter = faker.name(),
    )
    candidate.save()
    for _ in range(np.random.randint(5,10)):
        candidate.skill_set.create(name = faker.first_name())
    
def _create_fake_data():
    users = User.objects.all()
    if len(users)==0:
        _create_fake_user()
        users = User.objects.all()
    user = users[0]
    faker = Faker()
    for _ in range(100):
        job = Job()
        job.title = faker.catch_phrase()
        job.company = faker.company()
        job.owner = user
        job.job_type = np.random.choice([job_type[0] for job_type in Job.JOBS_TYPE])
        job.experiences = f"lev{np.random.randint(1,5)}"
        job.summary = faker.text(max_nb_chars = 2000)
        job.requierements = faker.text(max_nb_chars = 2000)
        job.date_created = timezone.now()
        job.location = faker.street_address()
        job.save()
        