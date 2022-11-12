from django.urls import path

from . import views

app_name = 'mensagens'

urlpatterns = [
    path('', views.index, name='index'),
    path('nova-mensagem/', views.nova_mensagem, name='nova_mensagem'),
]
