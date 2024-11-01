from django.shortcuts import render
from django.http.request import HttpRequest
from task1.forms import UserRegister
from task1.models import Buyer, Game, Station

# Create your views here.

def moscow_view(request):
    page_name = "МОСКОВСКОЕ МЕТРО"
    stations = [station.name for station in Station.objects.filter(city="moscow")]
    context = {
        "page_name": page_name,
        "stations": stations
    }
    return render(request, "moscow.html", context)

def petersburg_view(request):
    page_name = "ПЕТЕРБУРГСКОЕ МЕТРО"
    stations = [station.name for station in Station.objects.filter(city="saint-petersburg")]
    context = {
        "page_name": page_name,
        "stations": stations
    }
    return render(request, "saint-petersburg.html", context)

def menu_view(request):
    metros = {"moscow": "Москва", "saint-petersburg": "Санкт-Петербург"}
    context = {
        "metros": metros,
    }
    return render(request, "menu.html", context)


def sign_up(request: HttpRequest):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        print(form.errors)
        if form.is_valid():
            info["form"] = form
            users = Buyer.objects.all()
            users_names = [buyer.name for buyer in users]
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if password == repeat_password and name not in users_names:
                Buyer.objects.create(name=name, balance=0, age=age)
                info["error"] = f"Приветствуем, {name}"
                print(name, ",", password, ",", age)
            elif password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif name in users_names:
                info["error"] = "Пользователь с таким логином уже есть"
            else:
                info["error"] = "Что-то пошло не так..."

    else:
        form = UserRegister()
        info["form"] = form
    context = {
        "info": info,
    }
    return render(request, "registration_page.html", context)

