from django.contrib import admin
from .models import State, Profile, Order

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number', 'address')
    search_fields = ('user',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'origin', 'destination', 'fluid_quantity', 'distance', 'price')
    search_fields = ('user__username', 'origin__name', 'destination__name')
    list_filter = ('origin', 'destination')