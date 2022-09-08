from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def saludo(request):

    template = loader.get_template("myapp\miprimer.html")

    return HttpResponse(template.render())