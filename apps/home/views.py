from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView, FormView, View, ListView
from apps.home.forms import LoginForm,SignupForm

from .models import Users

from django.utils.decorators import method_decorator
from apps.home.decorators import check_user_auth

class IndexView(TemplateView):
    template_name = 'home/index.html'
    def get(self, request):
        if ('is_authenticated' not in request.session) or request.session['is_authenticated'] == 0:
            return render(self.request,"home/index.html")           
        else:
            return redirect(reverse('reports:index'))

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registeration/login.html'
    def form_valid(self, form):
        self.request.session['is_authenticated'] = 1
        self.request.session['email'] = self.request.POST['email'] 
        return redirect(reverse('reports:index'))

class SignupView(FormView):
    form_class = SignupForm
    template_name = 'registeration/signup.html'
    def form_valid(self, form):
        new_user = form.save()
        if(new_user):
            new_user.save()
            return redirect(reverse('home:index'))
        else:
            return redirect(reverse('home:signup'))
class SignupView(FormView):
    form_class = SignupForm
    template_name = 'registeration/signup.html'
    def form_valid(self, form):
        new_user = form.save()
        if(new_user):
            new_user.save()
            return redirect(reverse('home:index'))
        else:
            return redirect(reverse('home:signup'))

class LogoutView(View):
    def get(self,request):
        print("logout")
        request.session['is_authenticated'] = 0
        return redirect(reverse('home:index'))