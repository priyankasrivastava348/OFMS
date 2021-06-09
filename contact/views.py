from django.shortcuts import render

# Create your views here.
def contactfun (request):
	return render(request,'contact.html')

