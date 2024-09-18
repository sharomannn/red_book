from django.db import models
from core import consts


class Sector(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название сектора")
    code = models.CharField(max_length=255, verbose_name="Код сектора")
    description = models.TextField(blank=True, null=True, verbose_name="Описание сектора")

    public_latitude = models.FloatField(verbose_name="Широта")
    public_longitude = models.FloatField(verbose_name="Долгота")

    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сектор"
        verbose_name_plural = "Сектора"


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Отряд")
    description = models.TextField(blank=True, null=True, verbose_name="Описание отряда")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отряд"
        verbose_name_plural = "Отряды"

class Family(models.Model):
    name = models.CharField(max_length=100, verbose_name="Семейство")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="families", verbose_name="Отряд")
    description = models.TextField(blank=True, null=True, verbose_name="Описание семейства")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Семейство"
        verbose_name_plural = "Семейства"

class RedBookEntry(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    latin_name = models.CharField(max_length=200, verbose_name="Латинское название")
    category = models.CharField(max_length=1, choices=consts.CATEGORY.CHOICES, verbose_name="Категория")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="entries", verbose_name="Отряд")
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="entries", verbose_name="Семейство")
    description = models.TextField(verbose_name="Описание")

    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Сектор")
    image = models.ImageField(upload_to='red_book_images/', blank=True, null=True, verbose_name="Фото")
    public = models.BooleanField('Опубликованная информация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись в Красной книге"
        verbose_name_plural = "Записи в Красной книге"

class Observation(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    category = models.CharField(max_length=20, choices=consts.CATEGORY.CHOICES, verbose_name="Категория")
    location = models.CharField(max_length=200, verbose_name="Место")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")
    description = models.TextField(max_length=1000, verbose_name="Описание", blank=True)
    photo = models.ImageField(upload_to='observations/', blank=True, null=True, verbose_name="Фото")
    observer_name = models.CharField(max_length=200, verbose_name="Ваше ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    date_time = models.DateTimeField(verbose_name="Дата и время наблюдения")

    processed = models.BooleanField(default=False, verbose_name="Обработанное")
    erroneous = models.BooleanField(default=False, verbose_name="Ошибочное наблюдение")

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = "Наблюдение"
        verbose_name_plural = "Наблюдения"
