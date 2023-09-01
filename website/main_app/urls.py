from django.urls import path
from .views import *


urlpatterns = [
    path('', MainHomePage.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<slug:shop_slug>/', ShopChoice.as_view(), name='shop'),
    path('<slug:shop_slug>/<slug:cat_slug>', CatigoryChoise.as_view(), name='cat')
]
