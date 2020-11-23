from django.shortcuts import render
from . import models

def index(request):
    template_name = "copystockApp/index.html"
    context = {"articles": models.Article.objects.all()}
    return render(request, template_name, context)

def new(request):
    template_name = "copystockApp/new.html"
    if request.method == "POST":
        models.Article.objects.create(title=request.POST["title"])
    return render(request, template_name)