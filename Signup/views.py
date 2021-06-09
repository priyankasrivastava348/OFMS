from django.shortcuts import render,redirect
from django . http import HttpResponse 
from django.contrib import messages
from . models import MyUser 
# Create your views here.

def signupfun ( request ) : 

	return render ( request , 'signup.html')
def signupsavefun ( request ) :

	print ( request . GET )
	print ( request . POST )
	if request . method == 'GET' : 
		return redirect ( 'signup')


	elif request . method == 'POST'  :

	#return render ( request , 'signupsuc.html', {'username' : request . POST ['username'] })
		if len ( MyUser . objects . filter ( username = request . POST ['username']) ) == 0 :
			obj = MyUser ( first_name = request . POST ['first_name'], last_name = request . POST['last_name'],\
		 username = request . POST['username'], password = request . POST ['password'] , address = request . POST ['address'])
			obj . save () 
			messages.success(request, 'Your signup handaled successfully!')
		else : 
			messages.error ( request , 'Username is allready taken  . . ! ') 
		return redirect ( 'login' )

