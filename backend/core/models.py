from django.contrib.auth.models import AbstractUser
from django.db import models

from core import consts


class User(AbstractUser):
    patronymic = models.CharField('отчество', max_length=255, blank=True)
    birthday = models.DateField('дата рождения', blank=True, null=True)
    is_moderator = models.BooleanField('модератор', default=False)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username


class Sector(models.Model):
    name = models.CharField('название сектора', max_length=255)
    code = models.CharField('код сектора', max_length=255, blank=True, null=True)
    description = models.TextField('описание сектора', blank=True, null=True)
    sector_type = models.CharField(
        'тип сектора', max_length=255, choices=consts.SECTOR_TYPES.CHOICES, blank=True, null=True
    )

    latitude = models.FloatField('широта', blank=True, null=True)
    longitude = models.FloatField('долгота', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сектор'
        verbose_name_plural = 'сектора'


class Order(models.Model):
    name = models.CharField('отряд', max_length=100)
    description = models.TextField('описание отряда', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'отряд'
        verbose_name_plural = 'отряды'


class Family(models.Model):
    name = models.CharField('семейство', max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='families', verbose_name='отряд')
    description = models.TextField('описание семейства', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'семейство'
        verbose_name_plural = 'семейства'


class Section(models.Model):
    name = models.CharField('раздел', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'


class RedBookEntry(models.Model):
    name = models.CharField('название', max_length=200)
    latin_name = models.CharField('латинское название', max_length=200, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True, related_name='entries')
    category = models.CharField('категория', max_length=1, choices=consts.CATEGORY.CHOICES, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='entries', verbose_name='отряд', blank=True, null=True
    )
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name='entries', verbose_name='семейство', blank=True, null=True
    )
    description = models.TextField('описание', blank=True, null=True)

    sector = models.ManyToManyField(Sector, verbose_name='сектора', related_name='red_book_entry', blank=True)
    image = models.ImageField('фото', upload_to='red_book_images/', blank=True, null=True)
    public = models.BooleanField('опубликованная информация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'запись в красной книге'
        verbose_name_plural = 'записи в красной книге'


class Observation(models.Model):
    name = models.CharField('название', max_length=200)
    category = models.CharField('категория', max_length=20, choices=consts.CATEGORY.CHOICES, blank=True, null=True)
    location = models.CharField('место', max_length=200, blank=True, null=True)
    latitude = models.FloatField('широта', blank=True, null=True)
    longitude = models.FloatField('долгота', blank=True, null=True)
    description = models.TextField('описание', max_length=1000, blank=True)
    photo = models.ImageField('фото', upload_to='observations/', blank=True, null=True)
    observer_name = models.CharField('ваше ФИО', max_length=200, blank=True, null=True)
    phone_number = models.CharField('номер телефона', max_length=20, blank=True, null=True)
    date_time = models.DateTimeField('дата и время наблюдения', blank=True, null=True)

    status = models.BooleanField('обработанное/необработанное', default=False)
    erroneous = models.BooleanField('ошибочное наблюдение', default=False)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'наблюдение'
        verbose_name_plural = 'наблюдения'
