from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class login_call(MiddlewareMixin):
    def process_request(self, request):
	context={}
	if request.path in ['/login/', '/register/']  or request.user.is_authenticated():
		return
	else:		
        	return redirect('/login/')
