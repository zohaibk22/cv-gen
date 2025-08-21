from django.db import models

# Create your models here.


class ResumeDetailsModel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Full Name", blank=False, null=False)
    email = models.EmailField(max_length=200, verbose_name="Email Address", blank=False, null=False)
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", blank=False, null=False)
    summary = models.TextField(max_length=200, verbose_name="Summary", blank=False, null=False)
    degree = models.CharField(max_length=200, verbose_name="Degree", blank=False, null=False)
    school = models.CharField(max_length=200, verbose_name="School", blank=False, null=False)
    university = models.CharField(max_length=200, verbose_name="University", blank=False, null=False)
    previous_work = models.TextField(max_length=1000, verbose_name="Previous Work Experience", blank=True, null=True)
    skills = models.TextField(max_length=1000, verbose_name="Skills", blank=True, null=True)

