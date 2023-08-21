from django.urls import path
from .views import *

urlpatterns = [
    path('', MainHomePage.as_view(), name='main'),
    path('', MainHomePage.as_view(), name='feedback'),
    path('', MainHomePage.as_view(), name='about'),
    path('', MainHomePage.as_view(), name='home'),
]
