from django.db import models

MEASURE_CHOICES = (
    (0, u'гр.'),
    (1, u'мл.'),
)

class Item(models.Model):
    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"
    name = models.CharField(verbose_name="Наименование", max_length=250)
    weight = models.PositiveIntegerField(verbose_name="Вес", default=None, blank=True, null=True)
    measure = models.PositiveIntegerField('Ед. измерения', default=0, blank=False, null=False, choices=MEASURE_CHOICES)
    descr = models.CharField(verbose_name="Описание", max_length=5250, default=None, blank=True, null=True)
    sostav = models.CharField(verbose_name="Состав", max_length=5250, default=None, blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name="Цена", default=None, blank=True, null=True)
    oldprice = models.PositiveIntegerField(verbose_name="Перечеркнутая цена", default=None, blank=True, null=True)

    href = models.CharField(verbose_name="код для ссылки", max_length=64, unique=True, null=False, blank=False)


    def __str__(self):
        return str(self.name)

