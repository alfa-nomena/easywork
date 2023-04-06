from django.shortcuts import render
from .models import Job
from faker import Faker
from django.contrib.auth.models import User
import numpy as np
from django.utils import timezone
from users.models import Candidate
from django.views.generic.list import ListView



class ListAllJobsView(ListView):
    model=Job
    paginate_by=20
    template_name = 'jobs/list-all-jobs.html'
    context_object_name='jobs'
    


def home(request):
    jobs = Job.objects.all()
    if len(jobs)<5:
        _create_fake_data()
        jobs = Job.objects.all()
    context = {
        "jobs":jobs[:5]
    }
    user = request.user
    if user.is_authenticated:
        
        if candidate := Candidate.objects.filter(user=user):
            context['candidate'] = candidate[0]
    template = 'jobs/index.html'
    print(jobs[0].get_job_type_display())
    return render(request, template, context)

def _create_fake_user():
    user = User.objects.create_user(username='test', password='test')
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(user.id, user.username, user.password)
    
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