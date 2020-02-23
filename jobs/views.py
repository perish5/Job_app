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

class JobsDetail(DetailView):
    model = Jobs
    template_name = "jobs/single_jobs.html"
    context_object_name = "detail_jobs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object.count = self.object.count + 1  # to count views
        # self.object.save()
        context["popular_jobs"] = Jobs.objects.order_by("-count")[:4]
        return context

        # front page ko trending news haru ma latest news dekhauna and dynamic banauna
class JobsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        print(categories)
        category_jobs_list = {}
        for category in categories:
            # context[category.title] = News.objects.filter(category=category)
            category_jobs_list[category] = Jobs.objects.filter(category=category)
        context["jobs_list"] = Jobs.objects.all().order_by("-created_at")[:4] # - le last ma added latest news haru dekhaua first ma
        context["trending_jobs"] = Jobs.objects.order_by("-count")
        context["category_jobs_list"] = category_jobs_list
        print(context)
        return context