from django.shortcuts import render
from apps.recipes.models import Recipe, Category

def home(request):
    print request
    recipes = Recipe.objects.filter(category__slug__contains='mains')
    print recipes

    return render(request, 'home.html',
    {
        'recipes': recipes,
    })


def category(request, category_slug):
    recipes = Recipe.objects.filter(category__slug=category_slug)

    return render(request, 'category.html', {
      'recipes': recipes,
    })

def recipe(request, category_slug, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    return render(request, 'recipe.html', {
      'recipe': recipe,
    })
