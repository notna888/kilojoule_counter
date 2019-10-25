import csv
import os

from django.http import HttpResponse
from django.shortcuts import render

from .models import Meal, Ingredient, Ingredient_Meal
from .forms import IngredientForm


def all_meals(request):
    all_meals = Meal.objects.all()
    context = {
        'meals' : all_meals
    }

    return render(
        request=request,
        template_name="all_meals.html",
        context=context
    )

def all_ingredients(request):
    ingredients = Ingredient.objects.all()

    ingred_list = [str(i) for i in ingredients]

    return HttpResponse('<br>'.join(ingred_list))


def load_ingredients(request):
    csv_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'starting_data/')
    # print(csv_folder)
    with open(csv_folder + 'ingredients.csv') as ingredient_file:
        ingredient_csv = csv.reader(ingredient_file)

        row_number = 0
        for row in ingredient_csv:
            if(row_number):
                print(row)
                created, ingredient_obj = Ingredient.objects.get_or_create(
                    ingredient_name = row[0],
                    ingredient_kilojoule = row[1]
                )
                print(created)
            else:
                header_row = row
                print('header row', header_row)
            row_number += 1


    return HttpResponse('Ingredients Loaded Successfully')

def load_meals(request):
    return HttpResponse('Not implimented yet')


def edit_ingredients(request):
    ing_form = IngredientForm()

    context = {
        'form' : ing_form,
    }

    print("blah??")

    return render(
        request=request,
        template_name="edit_forms/ingredient_form.html",
        context=context
    )
