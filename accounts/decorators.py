from django.http import HttpResponse
from django.shortcuts import redirect
from verification.models import Verification

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('verify')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def unverified_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		user = Verification.objects.get(user = request.user)
		if user.status:
			return redirect('dashboard')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)

			if group == '':
				return HttpResponse('You are not in any group! please contact support')

			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def auto_routers(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'Student':
			return HttpResponse('You are not authorized to view this page')

		if group == 'Lessor':
			return HttpResponse('You are not authorized to view this page')

		else:
			return view_func(request, *args, **kwargs)

	return wrapper_function