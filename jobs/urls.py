from django.urls import path
from django.conf import settings
from jobs import views

urlpatterns = [
    path("<category_id>/",views.CategoryView.as_view(),name="category_jobs"),
    path("<category_id>/",views.CategoryJobsView.as_view(),name="categorie_jobs"),
]
