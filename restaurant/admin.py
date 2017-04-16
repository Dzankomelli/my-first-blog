from django.contrib import admin
from restaurant.models import Food, Wine, WineCategory, FoodCategory

admin.site.register(Food)
admin.site.register(WineCategory)
admin.site.register(Wine)
admin.site.register(FoodCategory)
# Register your models here.
