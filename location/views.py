from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from .forms import InputForm

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            ip=form.cleaned_data['IP']
            return HttpResponseRedirect('/'+str(ip))
    else:
        form = InputForm()

    return render(request,'location/index.html',{
        'form':form,
    })


def result(request,ip_address):
    #ip=str(s1)+"."+str(s2)+"."+str(s3)+"."+str(s4)
    response = requests.get('http://ip-api.com/json/'+ip_address)
    data = response.json()

    return render(request,'location/result.html',{
        'status':data['status'],
        'city':data['city'],
        'country':data['country'],
        'regionName':data['regionName'],
        'zip':data['zip'],
    })
