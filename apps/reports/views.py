from django.shortcuts import render
from django.utils.decorators import method_decorator
import mws
from kiffert import settings
from django.views.generic import TemplateView, FormView, View, ListView
# Create your views here.
from apps.home.decorators import check_user_auth

@method_decorator(check_user_auth, name='dispatch')
class IndexView(TemplateView):
	template_name = 'reports/index.html'
	def get(self,request):
		order_api = mws.Orders(
			access_key=settings.MWS_ACCESS_KEY,
			secret_key=settings.MWS_SECRET_KEY,
			account_id=settings.MWS_ACCOUNT_ID,
			region='IN',
			)
		service_status = order_api.get_service_status()
		print(service_status.parsed)
		context = {'email': self.request.session['email']}
		return render(self.request,"reports/index.html",context)ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss