from django.db import models

# Create your models here.
class StatusCRM(models.Model):
    status_name=models.CharField(max_length=64, verbose_name="Текущий статус")

    def __str__(self) -> str:
        return self.status_name
    class Meta:
        verbose_name='Статус'
        verbose_name_plural='Статусы'


class Order(models.Model):
    order_date= models.DateTimeField(auto_now=True, verbose_name='Дата')
    order_name=models.CharField(max_length=200, verbose_name='Имя')
    order_phone=models.CharField(max_length=30, verbose_name='Телефон')
    order_status=models.ForeignKey(StatusCRM, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self) -> str:
        return self.order_name
    
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

class CommentCRM(models.Model):
    comment_bind=models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Комментарий')
    comment_txt=models.TextField(verbose_name='Комментарий')
    comment_date=models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __str__(self) -> str:
        return self.comment_txt
    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'