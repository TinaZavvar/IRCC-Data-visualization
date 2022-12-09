from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:user_id>', views.subscription_detail),
    path('update/<str:sub_id>', views.subscription_update),
]