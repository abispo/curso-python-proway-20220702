from django.shortcuts import render
from django.contrib.auth.models import User


def new(request):
    if request.method == 'GET':
        return render(request, 'register/new.html')
    elif request.method == 'POST':
        post_data = request.POST

        u = User(
            username=post_data.get('txtUsername'),
            email=post_data.get('txtEmail'),
            first_name=post_data.get('txtFirstName'),
            last_name=post_data.get('txtLastName')
        )

        # Criptografa a senha do usuário. Isso é necessário para o usuário
        # poder fazer o login
        u.set_password(post_data.get("txtPassword"))
        u.save()

        return render(request, 'register/success.html')
