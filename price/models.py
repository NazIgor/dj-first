from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_title=models.CharField(max_length=30, verbose_name='Название')
    pc_descipt=models.CharField(max_length=256, verbose_name='Описание')
    pc_price=models.CharField(max_length=128,verbose_name='Цена за пакет')

    def __str__(self) -> str:
        return self.pc_title
    class Meta():
        verbose_name='Пакет'
        verbose_name_plural='Пакеты'

class PriceTable(models.Model):
    pt_name=models.CharField(max_length=128, verbose_name='Название')
    pt_old_price=models.CharField(max_length=128,verbose_name='Старая цена')
    pt_price=models.CharField(max_length=128,verbose_name='Цена')

    def __str__(self) -> str:
        return self.pt_name
    class Meta():
        verbose_name='Услуга'
        verbose_name_plural='Услуги'
