from django.shortcuts import render
from .models import Order
from .form import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelega


def first_page(request):
    form=OrderForm()
    slider_list=CmsSlider.objects.all()
    pc_all=PriceCard.objects.all()
    pc=pc_all[0:3]
    pt=PriceTable.objects.all()
    data={
        'slider_list':slider_list,
        'pc':pc,
        'pt':pt,
        'form':form
    }
    return render(request,'./index.html',data )

def thanks_page(request):    
    name=request.POST['name']
    phone=request.POST['phone']
    if name and phone:
        element=Order(order_name=name, order_phone=phone)
        element.save()
        sendTelega(tg_name=name, tg_phone=phone)
        text=' ваши данные отправленны на сервер'
    else:
        name=''
        phone=''
        text='Отсутсвуют несколько данных, проверьте форму'
    
    return render(request,'./thanks.html', {'name':name, 'phone':phone, 'text':text})