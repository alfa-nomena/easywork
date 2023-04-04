from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Job (models.Model):
    
    JOBS_TYPE = [
        ('FT', "Full time"),
        ('PT', "Part time"),
        ('RT', 'Remote')
    ]
    EXPS = [
        ('lev1', 'Less than 2 years'),
        ('lev2', '2 to 5 years'),
        ('lev3', '5 to 10 years'),
        ('lev4', 'More than 10 years'),
    ]
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOBS_TYPE)
    experiences = models.CharField(max_length=50, choices=EXPS)
    summary = models.TextField()
    requierements = models.TextField()
    logo = models.ImageField(upload_to='job', null=True, blank=True, default='job/unknown.jpg')
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("job")
        verbose_name_plural = ("jobs")

    def __str__(self):
        return f"{self.company} - {self.title}/{self.date_created.strftime('%Y-%m-%d')}"

