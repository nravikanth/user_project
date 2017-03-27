from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json
from .models import Book, UserProfile
from .forms import *
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
                post_data = request.POST.dict()	
                username = post_data.get('username')
                if User.objects.filter(username=username):
					return HttpResponse("User already exists")
                password = post_data.get('password')
                firstname = post_data.get('firstname')
                lastname = post_data.get('lastname')
                age = post_data.get('age')
                address = post_data.get('address')
		user_obj = User.objects.create_user(username=username, password=password)
		userprofile_obj = UserProfile.objects.create(user=user_obj,firstname=firstname,lastname=lastname,age=age,address=address)
		return HttpResponse("success")


def login_method(request):
	context={}
	if request.method=='GET':
		return render(request, 'new_login.html')
	else:
		pdb.set_trace()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			context['user_details'] = user.user_profile
			return render(request,"logged_in_user.html", context)
		else:
			return HttpResponse("Log in Failed")

def book_view(request):
	context = {}
	context['form_name']='Book Entry Form'
	if request.method=='POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("success")
	else:
		form = BookForm()
	context['form'] = form
	return  render(request, "form.html",context=context)

def publication_view(request):
    context={}
    context['form_name']='Publication Entry Form'
    if request.method=='POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    else:
        form = PublicationForm()
	context['form']=form
	return  render(request, "form.html",context=context)

		
		
		
