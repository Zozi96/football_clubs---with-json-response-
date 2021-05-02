from django.contrib import admin

from apps.club.models import Country, Club, League


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'league',)
    ordering = ('name', 'league',)


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    ordering = ('name', 'country',)
