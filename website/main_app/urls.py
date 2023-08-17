from django.urls import path
from .views import *

urlpatterns = [
    path('', MainHomePage.as_view(), name='home')
]
