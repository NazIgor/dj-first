from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    cms_img=models.ImageField(upload_to='media/slider_img/')
    cms_title=models.CharField(max_length=30, verbose_name='Заголовок')
    cms_text=models.CharField(max_length=128, verbose_name='Описание')
    cms_cssstyle=models.CharField(max_length=256, null=True, default='-', verbose_name='CSS')


    def __str__(self) -> str:
        return self.cms_text
    
    class Meta:
        verbose_name='Слайд'
        verbose_name_plural='Слайдер'