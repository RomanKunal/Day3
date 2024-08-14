from django.shortcuts import render

def dataFromProject(request):
    data={
        'name':'Akshira',
        'age':19,
        'city':'Australia'
    }
    return render(request,'output.html',data)