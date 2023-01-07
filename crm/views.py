from django.shortcuts import render
from .models import Order
from .form import OrderForm



def first_page(request):
    order_list=Order.objects.all()
    form=OrderForm()
    return render(request,'./index.html',{'order_list':order_list, 'form':form})

def thanks_page(request):    
    name=request.POST['name']
    phone=request.POST['phone']
    if name and phone:
        element=Order(order_name=name, order_phone=phone)
        element.save()
        text=' ваши данные отправленны на сервер'
    else:
        name=''
        phone=''
        text='Отсутсвуют несколько данных, проверьте форму'
    
    return render(request,'./thanks.html', {'name':name, 'phone':phone, 'text':text})