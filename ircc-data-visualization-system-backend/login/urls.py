from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register),
    path('update/<str:id>', views.user_detail),
    path('', views.check_login)
]