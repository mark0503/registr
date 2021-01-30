from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('auth/', views.auth, name='auth'),
    path('accounts/profile/', views.profile, name="profile"),
    path('looogout/', views.ouut, name="out")
]
