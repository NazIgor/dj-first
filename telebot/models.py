from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token=models.CharField(max_length=200, verbose_name='Токен')
    tg_chat=models.CharField(max_length=200, verbose_name='Чат ID')
    tg_txt=models.TextField(verbose_name='Текст сообщения')

    def __str__(self) -> str:
        return self.tg_chat
    class Meta:
        verbose_name="Настройку"
        verbose_name_plural="Настройки"
