from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4
from django.template.defaultfilters import slugify




class Job (models.Model):
    TYPES = [
        ('full-time', "Full time"),
        ('part-time', "Part time"),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]
    EXPERIENCES = [
        ('lev1', 'Less than 2 years'),
        ('lev2', '2 to 5 years'),
        ('lev3', '5 to 10 years'),
        ('lev4', 'More than 10 years'),
    ]
    identifiant = models.CharField(blank=True, null=True, max_length=100)
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=TYPES)
    experiences = models.CharField(max_length=50, choices=EXPERIENCES)
    summary = models.TextField()
    requierements = models.TextField()
    logo = models.ImageField(upload_to='job', null=True, blank=True, default='jobs/pictures/unknown.jpg')
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    salary_min = models.IntegerField(default=0, blank=True, null=True)
    salary_max = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        verbose_name = ("job")
        verbose_name_plural = ("jobs")

    def __str__(self):
        return f"{self.company} - {self.title}/{self.date_created.strftime('%Y-%m-%d')}"

    def salary(self):
        salary = ""
        if self.salary_min>0:
            salary == f"${self.salary_min}"
            if self.salary_max>self.salary_min:
                salary += f" - {self.salary_max}"
        return salary

    def save(self, *args, **kwargs):
        if self.identifiant is None:
            self.identifiant = str(uuid4()).split("-")[-1]
        
        self.slug = slugify(f"{self.company} {self.title} {self.identifiant}")
        return super(Job, self).save(*args, **kwargs)
    
    @staticmethod
    def experiences_choices(self):
        return self.EXPS