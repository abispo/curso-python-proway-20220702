from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('new/', views.new, name='new')
]
