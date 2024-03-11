import logging

from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RecipeForm
from .models import Recipe

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    recipes = Recipe.objects.all()[:5]
    return render(request, 'recipes_app/index.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipes_app/recipe_detail.html', {'recipe': recipe})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            logger.info(f'Получили{recipe=}, автор{recipe.author=}')
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipes_app/add_recipe.html', {'form': form})
    # return render(request, 'recipes_app/add_recipe.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Редирект на главную страницу после входа
        else:
            # Обработка неправильных учетных данных
            # Можно вывести сообщение об ошибке или редирект на другую страницу
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('/')  # Редирект на главную страницу после выхода

def login_view(request):
    if request.method == 'POST':
        # Логика для обработки POST-запроса при входе
        pass
    else:
        # Логика для отображения формы входа при GET-запросе
        return render(request, 'registration/login.html')

    return HttpResponse('Success')  # Вернуть HttpResponse для POST-запроса