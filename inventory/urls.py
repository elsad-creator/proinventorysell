from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Əsas səhifə
    path('sign-in/', views.sign_in, name='sign_in'),  # Giriş səhifəsi
    path('dashboard/', views.dashboard, name='dashboard'),  # İdarəetmə paneli
    path('logout/', LogoutView.as_view(next_page='sign_in'), name='logout'),  # Çıxış
]