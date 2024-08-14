from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def call(request):
#     return HttpResponse("<h1>Aksh >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>anyone</h1>")

def dataFromDB(request):
    data={
        'name':'Kunal',
        'age':18,
        'city':'NY'
    }
    return render(request,'output.html',data)
