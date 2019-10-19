from django.contrib import admin
from .models import *

class MealAdmin(admin.ModelAdmin):
    fields = ['meal_name']

class IngredientAdmin(admin.ModelAdmin):
    fields = ['ingredient_name', 'ingredient_kilojoule']

class MealIngredientAdmin(admin.ModelAdmin):
    fields = ['ingredient', 'ingredient_amount', 'meal']

admin.site.register(Meal, MealAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Ingredient_Meal, MealIngredientAdmin)
