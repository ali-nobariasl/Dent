from django.http import HttpResponse
from django.shortcuts import render
from Application.models import first
from Application.forms import firstform

def home(request):
    context = {'name':'ali'}
    return render(request,'home.html', context = context)

def page(request):
    ali = first.objects.all()
    context= {
        'ali': ali
    }
    return render(request,'page.html', context=context)


def firstformview(request):
    
    form = firstform()  
    context = {}
    context['form'] = form
    return render(request,'first.html', context = context)