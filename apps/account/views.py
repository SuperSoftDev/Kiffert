from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View, ListView
# Create your views here.
from django.utils.decorators import method_decorator
from apps.home.decorators import check_user_auth

@method_decorator(check_user_auth, name='dispatch')
class IndexView(TemplateView):
    template_name = 'account/index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['email'] = self.request.session['email']
        return context