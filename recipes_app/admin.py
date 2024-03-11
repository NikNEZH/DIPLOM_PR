from django.contrib import admin
from .models import Recipe, Category, RecipeCategory


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'cooking_time']


admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Category)
admin.site.register(RecipeCategory)
