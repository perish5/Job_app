from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from jobs.models import JobCategory, Category, Jobs
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
# Create your views here.

class CategoryView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "jobs/categories.html"
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_jobs_list = Jobs.objects.filter(category=category)
        return render(
            request, template_name, {"category_jobs_list": category_jobs_list, "category": category}
        )

class CategoryJobsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "jobs/categoriess.html"
        # category = JobCategory.objects.get(pk=category_id)
        category = get_object_or_404(JobCategory, pk=category_id)
        category_jobs_list = Jobs.objects.filter(category=category)
        return render(
            request, template_name, {"category_jobs_list": category_jobs_list, "category": category}
        )
