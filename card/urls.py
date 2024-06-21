from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('', views.get_all, name='cards'),
    path('<uuid:id>/', views.get, name='card'),
    path('add/', views.add, name='add'),
]