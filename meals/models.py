from django.db import models

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    ingredient_kilojoule = models.FloatField(verbose_name='Kilojoules Per 100g')


    def __str__(self):
        return self.ingredient_name + ' : ' + str(self.ingredient_kilojoule) + 'kj'

class Ingredient_Meal(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE
    )
    ingredient_amount = models.FloatField()
    meal = models.ForeignKey(
        'Meal',
        on_delete=models.CASCADE
    )

class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
