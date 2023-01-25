
from django.urls import path
from app import views


urlpatterns = [
    path('',views.home, name='home'),
    path('wish/<str:name>', views.wish, name='wish'),
    path('wish2/<str:name>', views.wish2, name='wish2'),
    path('create/', views.create, name='create'),
]