from django.shortcuts import render
from .models import Job
from faker import Faker
from django.contrib.auth.models import User
import numpy as np
from django.utils import timezone


def home(request):
    jobs = Job.objects.all()
    users = User.objects.all()
    if len(jobs)<5:
        _create_fake_data()
        jobs = Job.objects.all()
    context = {
        "jobs":jobs[:5],
        'nb_jobs' : len(jobs),
        'nb_users': len(users)
    }
    template = 'jobs/index.html'
    return render(request, template, context)





def _create_fake_user():
    user = User.objects.create_user(username='test', password='test')
    user.save()
    print(user.id, user.username, user.password)
    
def _create_fake_data():
    users = User.objects.all()
    if len(users)==0:
        _create_fake_user()
        users = User.objects.all()
    user = users[0]
    faker = Faker()
    job_types = ['FT', 'PT', "RT"]
    for _ in range(100):
        job = Job()
        job.title = faker.catch_phrase()
        job.company = faker.company()
        job.owner = user
        job.job_type=np.random.choice(job_types)
        job.experiences = f"lev{np.random.randint(1,5)}"
        job.summary = faker.text(max_nb_chars = 2000)
        job.requierements = faker.text(max_nb_chars = 2000)
        job.date_created = timezone.now()
        job.location = faker.street_address()
        job.save()