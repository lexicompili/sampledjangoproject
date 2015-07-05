from django.contrib import admin

# Register your models here.
from .models import Category, Recipe

admin.site.register(Category)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Recipe, RecipeAdmin) 
