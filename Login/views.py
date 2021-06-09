from django.shortcuts import render,redirect

from django . contrib import messages
from service . models import Order  
# Create your views here.

from Signup . views import MyUser 
def loginfun ( request ) : 

	return render ( request , 'login.html')

def dashboard ( request ) :

	print ( request . POST . get ('next'))
	print ( request . GET )
	print ( request . POST )
	if request . method == 'GET' : 
		return redirect ( 'login')


	elif request . method == 'POST':

		obj = MyUser . objects . filter ( username = request . POST ['username'], password = request . POST ['password'])

		if len ( obj ) == 1 :
			request . session ['username'] = request . POST ['username']
			orders = Order . objects . filter ( username = request . session [ 'username'])
			print ( orders . reverse ()  )
			return render ( request , 'loginsuc.html' , { 'username' : request . POST ['username'], 
				'status' : 'login',
				'orders' : orders [ : : -1 ]})
		else :
			messages . error ( request , 'Invalid User name or password !')
			return redirect ('login')

def logoutfun ( request ) : 
	request . session . clear () 
	return redirect ( 'home')
