from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.plan_create),
    path('update/<str:plan_id>', views.plan_detail),
]