from django import forms
from jobs.models import Category, Jobs, JobCategory
# from accounts.models import Profile, User



class JobsCreateForm(forms.ModelForm):
    CATEGORY_CHOICES = [(category.id, category.title) for category in Category.objects.all()]
    category = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=CATEGORY_CHOICES,
    )
    JOBCATEGORY_CHOICES = [(jobcategory.id, jobcategory.title) for jobcategory in JobCategory.objects.all()]
    jobcategory = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=JOBCATEGORY_CHOICES,
    )
    class Meta:
        model = Jobs
        fields = "title", "content", "cover_image", "category","jobcategory","company_name","address","salary","skills","education","experience","job_level","vacancy_no"
