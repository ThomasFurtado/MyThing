from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('delete/<str:pk>', views.delete, name='delete')
]