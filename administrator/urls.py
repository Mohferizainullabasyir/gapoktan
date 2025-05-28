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
    
    #ketua
    
    path('ketua/', views.ketuaadmin, name='ketuaadmin'),
    path('form-ketua/', views.formketuaadmin, name='formketuaadmin'),
    path('edit-ketua/<str:pk>', views.editketuaadmin, name='editketuaadmin'),
    path('delete-ketua/<str:pk>', views.deleteketuaadmin, name='deleteketuaadmin'),
    
    #ketua gapoktan
    
    path('form-ketuagapoktan/', views.formketuagapoktanadmin, name='formketuagapoktanadmin'),
    path('edit-ketuagapoktan/<str:pk>/', views.editketuagapoktanadmin, name='editketuagapoktanadmin'),
    path('delete-ketuagapoktan/<str:pk>/', views.deleteketuagapoktanadmin, name='deleteketuagapoktanadmin'),
    
    #anggota
    
    path('anggota/', views.anggotaadmin, name='anggotaadmin'),
    path('form-anggota/', views.formanggotaadmin, name='formanggotaadmin'),
    path('edit-anggota/<str:pk>', views.editanggotaadmin, name='editanggotaadmin'),
    path('delete-anggota/<str:pk>', views.deleteanggotaadmin, name='deleteanggotaadmin'),

]
