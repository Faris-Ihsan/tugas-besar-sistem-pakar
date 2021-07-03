from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from siskar_app.datamodels import modelsloader

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
            print("positif")
        else:
            print("negatif")

            
    return render(request,'index.html', {'form':form})
