from django.shortcuts import render
from service . models import Order 
from service . models import Item 
from service . models import Hotel 
from django.http import HttpResponse 
# Create your views here.

def getorderslist ( request , id ) : 
	hotel = Hotel . objects . get ( id = id )
	objs = Order . objects . filter ( hotel_id = id ) [ : : -1 ]

	objs = [ x for x in objs ]
	print ( objs )

	for x in objs : 
		y = eval ( x . item_ids )
		itn = y [ 0 ]
		itq = y [ 1 ]

		temp = zip ( itn , itq )

		xlist =  ( [ [ Item . objects . get ( id = x ) . item_name   , y] for x , y in temp if y != '' ] ) 

		x = x . __dict__ 
		x . update ( { 'xlist' : xlist })

	return render ( request , 'hotelorders.html', { 'data' : objs, 'hotel' : hotel })


