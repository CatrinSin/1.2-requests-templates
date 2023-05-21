from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    return HttpResponse("Выберите рецепт!")

def recipes_view(request, recipe_name):
    if recipe_name in DATA.keys():
        servings = request.GET.get('servings', 1)
        ingridients = {}
        for ingridient in DATA[recipe_name]:
            ingridients[ingridient] = round(DATA[recipe_name][ingridient] * int(servings), 2)
            context = {
            'recipe': ingridients
        }
    else:
        context = {}
    return render(request, 'calculator/index.html', context)

