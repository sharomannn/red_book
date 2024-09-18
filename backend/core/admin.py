from django.contrib import admin
from .models import Order, Family, RedBookEntry

# Регистрация модели Order (Отряды)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Регистрация модели Family (Семейства)
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'order__name')  # Добавлен поиск по имени отряда
    list_filter = ('order',)  # Фильтр по отряду

# Регистрация модели RedBookEntry (Записи в Красной книге)
@admin.register(RedBookEntry)
class RedBookEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'latin_name', 'category', 'order', 'family')
    search_fields = ('name', 'latin_name', 'order__name', 'family__name')  # Поиск по имени и таксономическим группам
    list_filter = ('category', 'order', 'family')  # Фильтры по категории, отряду и семейству
    ordering = ('name',)  # Сортировка по имени
