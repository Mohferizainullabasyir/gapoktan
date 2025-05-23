from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboardadmin'),
    
    path('profil/', views.profiladmin, name='profiladmin'),
    path('form-profil/', views.formprofiladmin, name='formprofiladmin'),
    path('edit-profil/<str:pk>', views.editprofiladmin, name='editprofiladmin'),
    path('delete-profil/<str:pk>', views.deleteprofiladmin, name='deleteprofiladmin'),
    
    # kegiatan
    
    path('form-kegiatan/', views.formkegiatanadmin, name='formkegiatanadmin'),
    path('edit-kegiatan/<str:pk>/', views.editkegiatanadmin, name='editkegiatanadmin'),
    path('delete-kegiatan/<str:pk>/', views.deletekegiatanadmin, name='deletekegiatanadmin'),
    
    #grup
    
    path('grup/', views.grupadmin, name='grupadmin'),
    path('form-grup/', views.formgrupadmin, name='formgrupadmin'),
    path('edit-grup/<str:pk>', views.editgrupadmin, name='editgrupadmin'),
    path('delete-grup/<str:pk>', views.deletegrupadmin, name='deletegrupadmin'),


]
