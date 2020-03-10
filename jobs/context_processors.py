from django.shortcuts import render
from jobs.models import JobCategory, Category
# category dekhauna jati ota xuttai category xa teti ota function banauna parxa
# ya 2 ota xa "jobcategory ra category" tei vayera 2 ota function banayo full time haru ra financial bankink dekhauna
def jobcategories(request):
    categorie_list = JobCategory.objects.all() # models.py ko jobcategory class ma vako  dekhuaxa
    return{"categorie":categorie_list}

def categories(request):
    category_list = Category.objects.all() # category ma vako sab dekhuaxa
    return{"categories":category_list}