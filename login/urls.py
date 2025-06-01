from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # jadi halaman utama
    path('logout/', views.logout_view, name='logout'),
]
