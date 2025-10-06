from django.shortcuts import render

def home(request):
    # Se já tiver modelo de links, pode buscar do banco e passar no contexto.
    # Ex.: from .models import Link; links = Link.objects.filter(visible=True).order_by('order')
    # Por enquanto, usa uma lista vazia:
    links = []
    return render(request, "home.html", {"links": links})

