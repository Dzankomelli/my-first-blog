from django.shortcuts import render
from restaurant.models import Food, FoodCategory, WineCategory, Wine


# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'Timotej'})


def meni(request):
    foods_in_categories = []
    # dobim vse kategorije.
    categories = FoodCategory.objects.all()

    for category in categories:
        food_from_category = Food.objects.filter(type=category)
        foods_in_categories.append({'category': category.name, 'foods': food_from_category})

        print(foods_in_categories)
    return render(request, 'meni.html', {'foods_in_categories': foods_in_categories})

def nasipodatki(request):
    return render(request, 'nasipodatki.html', )

def vinskakarta(request):
    wines_in_categories = []
    # dobim vse kategorije.
    categories = WineCategory.objects.all()

    for category in categories:
        wine_from_category = Wine.objects.filter(type=category)
        wines_in_categories.append({'category': category.name, 'wines': wine_from_category})

        print(wines_in_categories)
    return render(request, 'vinskakarta.html', {'wines_in_categories': wines_in_categories})


