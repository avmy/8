from django.db import models
from django.contrib import admin
from django.utils.http import format_html
from django.utils import timezone
from dgango.contrib.auth import get_user_model


class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_lenth=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите, если возможен торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.create.at.date() == timezone.now().date():
            created_time = self.create_at.time().strtime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}'
            )
        return self.create_at.strtime('%d:%m:%Y')


    @admin.display(description='изображение')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;">'. url=self.image.url
            )

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'
