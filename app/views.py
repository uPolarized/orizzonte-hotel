from django.shortcuts import render
from .models import Link

def home(request):
    links = Link.objects.filter(visible=True).order_by('order')
    return render(request, "app/home.html", {"links": links})
