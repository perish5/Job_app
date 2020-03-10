from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Job_Categories"

    def __str__(self):
        return self.title

class JobCategory(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Time_Categories"

    def __str__(self):
        return self.title


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    job_description = models.TextField(blank=True)
    education =  models.CharField(max_length=255,null=False,blank=True)
    experience = models.CharField(max_length=255,null=False,blank=True)
    skills = models.CharField(max_length=255,null=False,blank=True)
    job_level = models.CharField(max_length=255,null=False,blank=True)
    vacancy_no = models.IntegerField(blank=True, null=True)
    category = models.ManyToManyField("Category",related_name="jobs_categories")# string ma ralhya vani yo class tala ni kam garxa mathi pani
    jobcategory = models.ManyToManyField("JobCategory",related_name="job_categories")
    count = models.IntegerField(default=0)# trending news ko lgi views count garna
    slug = models.SlugField(max_length=255,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True)# on delete means edi tyo author le xodera gaye pani news delete nahuni...news company ko property ho
    created_at = models.DateTimeField(auto_now_add=True)# add garesi updae hunna,add garya time matra basxa
    address = models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=255,null=True)
    salary = models.CharField(max_length=255, null=True)
    cover_image = models.ImageField(upload_to="jobs", null=True)
    
    def get_absolute_url(self): # absolute_url gives direct jumb to object view
        return reverse("jobs_detail", kwargs={"pk": self.pk, "slug": self.slug})

    class Meta:
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.title