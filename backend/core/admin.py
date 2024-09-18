from django.contrib import admin
from .models import Sector, Order, Family, RedBookEntry, Observation, User

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sector_type', 'latitude', 'longitude')
    search_fields = ('name', 'code')
    list_filter = ('sector_type',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'order__name')
    list_filter = ('order',)

@admin.register(RedBookEntry)
class RedBookEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'latin_name', 'category', 'order', 'family', 'public')
    search_fields = ('name', 'latin_name', 'order__name', 'family__name')
    list_filter = ('category', 'order', 'family', 'public')
    filter_horizontal = ('sector',)

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'status', 'erroneous', 'date_time', 'observer_name')
    search_fields = ('name', 'category', 'location', 'observer_name')
    list_filter = ('status', 'erroneous', 'category', 'date_time')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_moderator')
    search_fields = ('username', 'email')
