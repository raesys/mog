from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('allmog/', views.all_mog, name='all_mog'),
]
