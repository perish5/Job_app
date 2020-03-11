from django.contrib import admin
from accounts.models import Profile, User
from jobs.models import Category, Jobs, JobCategory
# Register your models here.


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ("title","author","created_at","company_name","cover_image")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(JobCategory)