from django.contrib import admin

from jobs.models import Category, Jobs, JobCategory
# Register your models here.
# admin.site.register(Jobs)
admin.site.register(Category)
admin.site.register(JobCategory)
@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ("title","author","created_at","company_name","cover_image")
    prepopulated_fields = {"slug": ("title",)}