from django.shortcuts import render
from apps.recipes.models import Recipe, Category

def home(request):
    recipes = Recipe.objects.all()[:3]
    print recipes

    return render(request, 'home.html',
    {
        'recipes': recipes,
    })
