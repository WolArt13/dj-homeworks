from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'borsh': {
        'свекла, шт': 1,
        'картофель, шт': 3,
        'морковь, шт': 1,
        'капуста, г': 300,
        'сметана, ст.л.': 2,
    },
    'pancakes': {
        'мука, г': 200,
        'молоко, мл': 300,
        'яйца, шт': 2,
        'сахар, ст.л.': 2,
        'соль, щепотка': 1,
        'масло растительное, ст.л.': 1,
    },
    'salad': {
        'помидор, шт': 2,
        'огурец, шт': 1,
        'салатные листья, г': 50,
        'оливковое масло, ст.л.': 2,
        'соль, щепотка': 1,
    },
    'fried_chicken': {
        'куриное филе, г': 400,
        'чеснок, зубчик': 2,
        'соль, ч.л.': 1,
        'перец, ч.л.': 0.5,
        'растительное масло, ст.л.': 2,
    },
    'pizza': {
        'тесто для пиццы, г': 300,
        'томатный соус, ст.л.': 3,
        'сыр, г': 100,
        'колбаса, г': 100,
        'грибы, г': 50,
    },
    'soup': {
        'вода, л': 1.5,
        'картофель, шт': 3,
        'морковь, шт': 1,
        'лук, шт': 1,
        'вермишель, г': 100,
    },
    'smoothie': {
        'банан, шт': 1,
        'ягоды, г': 100,
        'молоко, мл': 200,
        'мёд, ст.л.': 1,
    }
}

TITLE_NAMES = {
    'omlet': 'Омлет',
    'pasta': 'Паста',
    'buter': 'Бутерброд',
    'borsh': 'Борщ',
    'pancakes': 'Блины',
    'salad': 'Салат',
    'fried_chicken': 'Жареная курица',
    'pizza': 'Пицца',
    'soup': 'Суп',
    'smoothie': 'Смузи',
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_page(request):
    context = {
        'dishes': TITLE_NAMES
    }
    return render(request, 'calculator/index.html', context)

def recipe_page(request, recipe):
    servings = int(request.GET.get('servings', 1))
    
    if recipe in DATA:
        adjusted_recipe = {ingredient: round(amount * servings, 3) for ingredient, amount in DATA[recipe].items()}
        context = {
            'recipe': adjusted_recipe,
            'dish': TITLE_NAMES[recipe],
            'servings': servings
        }
        return render(request, 'calculator/recipe.html', context)
    else:
        return render(request, 'calculator/404.html')

