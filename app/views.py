from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TTO=Topic.objects.get_or_create(topic_name=tn)
        if TTO[1]:
            return HttpResponse(f'{tn} object is created')
        else:
             return HttpResponse(f'{tn} object is already present')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['mail']
        TO=Topic.objects.get(topic_name=tn)
        TWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
        if TWO[1]:
            return HttpResponse(f'{name} object is created')
        else:
            return HttpResponse(f'{name} object is already present')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        pk=request.POST['pk']
        name=request.POST['name']
        aut=request.POST['aut']
        date=request.POST['da']
        PO=Webpage.objects.get(pk=pk)
        TAO=AccessRecord.objects.get_or_create(name=PO,author=aut,date=date)
        if TAO[1]:
            return HttpResponse(f'{aut} object is created')
        else:
            return HttpResponse(f'{aut} object is already present')
    return render(request,'insert_access.html',d)


def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        ltns=request.POST.getlist('tns')
        WEQS=Webpage.objects.none()
        for tn in ltns:
            WEQS=WEQS|Webpage.objects.filter(topic_name=tn)
        d1={'LWO':WEQS}
        return render(request,'display_webpage.html',d1)
     

    return render(request,'select_multiple.html',d)