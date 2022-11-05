from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),

    # Contas do usuário
    path('me/accounts/create', views.create_account, name='create_account'),
    path('me/accounts', views.list_accounts, name='list_accounts'),

    # Transações
    path('me/transactions/create', views.create_transaction, name='create_transaction'),
    path('me/transactions', views.list_transactions, name='list_transactions')
]
