from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def index(request):
    form = forms.FormName()
    return render(request,'index.html', {'form':form})
