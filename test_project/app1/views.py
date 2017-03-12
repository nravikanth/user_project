from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json
from .models import Book
import pdb
import pudb

# Create your views here.

def test_view(request):
#	l=[1,2,3,4,5]
	l={'a':1,'b':2,'c':3,'d':4}
	return render(request,'index.html', context={'data':l})

def test_extends_parent(request):
	return render(request,'parent.html')

def test_extends_child(request):
	return render(request,'child.html')

def test_get(request):
	pdb.set_trace()
	book_id = request.GET['book_id']
	obj = Book.objects.filter(id=book_id)
	if obj:
		obj=obj[0]
		return HttpResponse(obj.book)
	else:	
		return HttpResponse("Book with given book_id=%s found" %book_id)
def test_post(request):
	pudb.set_trace()
	if request.method=='GET':
		return render(request, 'test_post.html')
	else:
		name = request.POST['username']
		return HttpResponse(name)

def register(request):
        if request.method=='GET':
                return render(request, 'register.html')
        else:
                username = request.POST['username']
                password = request.POST['password']
		#user_obj = User.objects.create(username=username, password=password)
		user_obj = User.objects.create_user(username=username, password=password)
		user_obj.save()
                return HttpResponse("success")


def login_method(request):
	if request.method=='GET':
		return render(request, 'login.html')
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request,"logged_in_user.html")
		else:
			return HttpResponse("Log in Failed")
