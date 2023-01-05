from django.shortcuts import render
from .models import Order



def first_page(request):
    order_list=Order.objects.all()
    return render(request,'./index.html',{'order_list':order_list})