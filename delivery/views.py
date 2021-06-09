from django.shortcuts import render, redirect
from django.http import JsonResponse 
from . models import deliveryboy
from service . models import Order , Hotel
from django.core import serializers

# Create your views here.

def dborders ( request , id ):
	obj = deliveryboy . objects . filter ( id = id ) [ 0 ]
	objs = obj . currentorder . all () 
	return render ( request , 'db.html', { 'obj' : obj , 'orders' : objs })\


def dbupdateorderstatus ( request , dvid, oid  ) : 

	# print ( hid )
	print ( oid )
	print ( request . GET , request . POST )
	Order . objects . filter ( id = oid ) . update ( hotel_status = request . GET ['selected'])
	return redirect ( 'http://localhost:8000/delivaryboy/{}/' . format ( dvid ))


def checkneworder ( request ) : 
	dvtaken  = []
	[ dvtaken . extend ( i . currentorder . all () )  for i in deliveryboy . objects . all () ]
	
	orders = Order . objects . all ()  

	nottaken = [] 
	for order in orders : 
		if order not in dvtaken:
			nottaken . append ( { 'id' : order.id, 'order_address' : order.order_address, 'from' : Hotel . objects . get ( id = order.hotel_id ) .hotel_name + ' '+ Hotel . objects . get ( id = order.hotel_id ) .hotel_address }  )
	#print ( nottaken )
	return JsonResponse ( {'status' : nottaken })

def dbgetorder ( request, dvid, oid ) : 

	deliveryboy . objects . filter ( id = dvid ) [ 0 ] . currentorder . add ( Order . objects . get ( id = oid )) 
	return redirect ('http://localhost:8000/delivaryboy/{}/'.format ( dvid ))