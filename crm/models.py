from django.db import models

# Create your models here.
class Order(models.Model):
    order_date= models.DateTimeField(auto_now=True, verbose_name='Дата')
    order_name=models.CharField(max_length=200, verbose_name='Имя')
    order_phone=models.CharField(max_length=30, verbose_name='Телефон')

    def __str__(self) -> str:
        return self.order_name
    
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'