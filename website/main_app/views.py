from django.shortcuts import render
from django.views import View

menu = [
    {"title": "Главная", "url_name": "main"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "О нас", "url_name": "about"},
]


class MainHomePage(View):
    def get(self, request):
        context = {
            "title": "Главная",
            "menu": menu
        }
        return render(request, "main_app/index.html", context=context)


class AboutUsPage(View):
    def get(self, request):
        context = {
            "title": "Главная",
            "menu": menu
        }
        return render(request, "main_app/base.html", context=context)


class ContactPage(View):
    def get(self, request):
        context = {
            "title": "Главная",
            "menu": menu
        }
        return render(request, "main_app/base.html", context=context)
