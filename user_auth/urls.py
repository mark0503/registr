from django.urls import path
from . import views as auth_views
from django.contrib.auth import views as login_views


urlpatterns = [
    path('', auth_views.index, name="index"),
    path('auth/', auth_views.auth, name='auth'),
    path('accounts/profile/', auth_views.profile, name="profile"),
    path('looogout/', auth_views.outh, name="out"),
    path('login/', login_views.LoginView.as_view(), name='login'),
    path('logout/', login_views.LogoutView.as_view(), name='logout'),
]
