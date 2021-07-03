from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from siskar_app.datamodels import modelsloader
from django.contrib import messages

# Create your views here.


def index(request):
    inputan=[]
    form = forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            for i in range(20):
                inputan.append(int(form.cleaned_data['attrib_'+str(i+1)]))
        
        hasil = modelsloader.loadmodels(inputan)        
        
        if hasil == 1:
            messages.warning(request, 'Positif COVID-19')
        else:
            messages.warning(request, 'Negatif COVID-19')
        

            
    return render(request,'index.html', {'form':form})
