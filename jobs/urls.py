from django.urls import path
from django.conf import settings
from jobs import views

urlpatterns = [
    path("create/", views.JobsCreateView.as_view(), name="create_jobs"),
    path('', views.about, name='about'),
    
    path("<category_id>/",views.CategoryView.as_view(),name="category_jobs"),
    path("<jobcategory_id>/",views.CategoryJobsView.as_view(),name="jobcategory_jobs"),
    
    
    path("<int:pk>/<slug>/", views.JobsDetail.as_view(), name="jobs_detail"),
    path("update/<int:pk>", views.JobsUpdateView.as_view(), name="update_jobs"),
    path("delete/<int:pk>", views.JobsDeleteView.as_view(), name="delete_jobs"),
    # path("<pk>/<slug>/feedback/", views.jobs_feedback, name="feedback_jobs"),
    
]
