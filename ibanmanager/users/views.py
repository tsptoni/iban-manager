# -*- coding: utf-8 -*-


from django.shortcuts import render
from ibanmanager.users import models as user_models

def password_new(request, token):

    context = {}

    if request.method == 'POST':
        password = request.POST['password']
        print('{0}'.format(password))
        token = user_models.TokenResetPassword.objects.get(token=token)
        user = token.user
        user.set_password(password)
        user.save()
        token.delete()

        return render(request, 'users/reset_password_success.html', context)

    return render(request, 'users/password_new.html', context)

