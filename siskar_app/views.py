from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.


def index(request):
    a=[]
    form = forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            for i in range(19):
                a.append(form.cleaned_data['attrib_'+str(i+1)])
            print(a)

            
    return render(request,'index.html', {'form':form})
