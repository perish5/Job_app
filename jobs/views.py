
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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from jobs.forms import JobsCreateForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
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
    def get(self, request, *args, **kwargs):
        template_name = "jobs/time_categories.html"
        # category = JobCategory.objects.get(pk=category_id)
        jobcategory = get_object_or_404(JobCategory)
        jobcategory_jobs_list = Jobs.objects.filter(jobcategory=jobcategory)
        return render(
            request, template_name, {"jobcategory_jobs_list": jobcategory_jobs_list, "jobcategory": jobcategory}
        )




class JobsDetail(DetailView):
    model = Jobs
    templatee_name = "jobs/jobs_detail.html"
    context_object_name = "detail_jobs"

class Forcandidate(DetailView):
    model = Jobs
    templatee_name = "jobs/forcandidates.html"
    context_object_name = "candidate_jobs"



        # front page ko trending news haru ma latest news dekhauna and dynamic banauna
class JobsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        
        print(categories)
        category_jobs_list = {}
        for category in categories:
            
            category_jobs_list[category] = Jobs.objects.filter(category=category)
        context["jobs_list"] = Jobs.objects.all().order_by("-created_at")[:4] # - le last ma added latest news haru dekhaua first ma
        context["popular_jobs"] = Jobs.objects.order_by("-count")[:4]
        context["category_jobs_list"] = category_jobs_list
        print(context)
        return context


class JobsCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    template_name = "jobs/create.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    form_class = JobsCreateForm

    def form_valid(self, form):
        jobs = form.save(commit=False)
        title = form.cleaned_data["title"]
        slug = slugify(title)
        jobs.slug = slug
        jobs.author = self.request.user
        jobs.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class JobsUpdateView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields =  "title", "content", "cover_image", "category","jobcategory","company_name","address","salary","skills","education","experience","job_level","vacancy_no","job_description"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    template_name = "jobs/update.html"
    


class JobsDeleteView(LoginRequiredMixin, DeleteView):
    model = Jobs
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    template_name = "jobs/delete.html"
    
    def get(self,request,*args, **kwargs):
        return self.post(self,request,*args, **kwargs)



@login_required(login_url="accounts/login")
@require_http_methods(["POST"])
def news_feedback(request, *args, **kwargs):
    data = request.POST
    print(data)
    print("HERE:", data)
    jobs_id = kwargs.get("pk")
    jobs = get_object_or_404(Jobs, id=jobs_id)
    # comment = Comment.objects.create(news=news, feedback=data["feedback"], commenter=request.user)
    return render(request)
    

def about(request):  
    template = loader.get_template('jobs/about.html')
    return HttpResponse(template.render({"active_tab":"about","request":request})) 