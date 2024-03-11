from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

    def __str__(self):
        return f'Заголовок {self.title}, Тема {self.theme}'


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory')

    def __str__(self):
        return f'Заголовок {self.title}, Описание {self.description}, Шаги готовки {self.steps}, Время приготовления' \
               f'{self.cooking_time}, Автор статьи {self.author}, Категория {self.categories}'


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Рецепт{self.recipe}, категория {self.category}'