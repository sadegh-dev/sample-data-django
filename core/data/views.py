from django.shortcuts import render
from .models import DataEn


def index(request):
    data = DataEn.objects.all()
    context = {
        'data':data ,
    }
    return render(request,'data/index.html',context)
