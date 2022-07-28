from django.shortcuts import render
from .models import DataEn
from django.db.models import F

"""
def index(request):
    data = DataEn.objects.all()
    context = {
        'data':data ,
    }
    return render(request,'data/index.html',context)
"""

def index(request):
    data = DataEn.objects.filter(id =1) 
    context = {
        'data':data ,
    }
    return render(request,'data/index.html',context)