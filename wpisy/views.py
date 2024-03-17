from django.shortcuts import render
from .models import Wpis
from django.template.response import TemplateResponse

# Create your views here.
def blog(request):
    return TemplateResponse(request, 'lista_wpisów.html',
    {"wpisy": Wpis.objects.filter(active=True)})
