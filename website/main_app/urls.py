from django.urls import path,include
from .views import *

urlpatterns = [
    path('', MainHomePage.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('products/<slug:shop_slug>/', ShopsView.as_view(), name='shops'),
    path('products/<slug:shop_slug>/<slug:cat_slug>/', ProductsView.as_view(), name='products'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include('social_django.urls', namespace='social')),
]
