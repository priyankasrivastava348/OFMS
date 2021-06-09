from django.shortcuts import render

# Create your views here.
def homefun ( request ) : 

	if 'username' in request . session : 

		return render ( request , 'base.html', {'status' : 'login'})
	else : 
		return render ( request , 'base.html', {'status' : 'not login'}) 
