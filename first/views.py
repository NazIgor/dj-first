from django.shortcuts import render

def index(request):
    a='Hello World'
    text="it's first main page"
    return render(request,'index.html',{
        'a':a,
        'text':text
    })
    
    