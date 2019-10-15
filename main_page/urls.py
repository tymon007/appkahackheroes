from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('log_in/', views.log_in, name="log_in"),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('auth_login/', views.auth_login, name="auth_login"),
    path('me/', views.me, name="me"),
    path('timer/', views.timer, name="timer"),
    path('food/', views.food, name="food"),
    path('gas/', views.gas, name="gas"),
    path('power/', views.power, name="power"),
    path('water/', views.water, name="water"),
    path('credits/', views.credits, name="credits"),
]
