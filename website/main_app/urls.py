from django.urls import path
from .views import *

urlpatterns = [
    path('', MainHomePage.as_view(), name='main'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutUsPage.as_view(), name='about'),
]
