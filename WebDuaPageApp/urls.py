from django.urls import path
from . import views

urlpatterns = [
    path('', views.BerandaView.as_view(), name='beranda'),
    path('tentangkami/', views.TentangKamiView.as_view(), name='tentang kami')
]