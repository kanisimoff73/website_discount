from django.urls import path
from .views import *


urlpatterns = [
    path('', MainHomePage.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    # path('login/', LoginIn.as_view(), name='login'),
    # path('register', RegisterUser.as_view(), name='register')
]
