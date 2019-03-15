from functools import wraps

from django.urls import reverse
from django.utils.decorators import available_attrs
from django.shortcuts import redirect, render_to_response, render


def check_user_auth(function):
    def wrap(request, *args, **kwargs):
        if ('is_authenticated' not in request.session) or request.session['is_authenticated'] == 0:
            return redirect(reverse('home:login'))            
        else:
            return function(request, *args, **kwargs)
    return wrap