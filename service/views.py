from django.shortcuts import render , redirect
from . models import Hotel , Item , Order 
from django . http import HttpResponse, JsonResponse  
import json 
from delivery . models import deliveryboy
from Signup . models import MyUser
# Create your views here.


def gethotels ( request ) : 


	hotels = Hotel . objects . filter ( hotel_address__contains = request . GET ['address'])
	print ( [])
	if 'username' in request . session :
		return render ( request , 'hotels.html', {'hotels' : hotels , 'status' : 'login'})
	else :  
		return render ( request , 'hotels.html', {'hotels' : hotels , 'status' : 'not login'})


def getitems ( request, id ) : 


	if 'username' in request . session : 
		request . session ['hotelid'] = id 
		items = Item . objects . filter ( hotel = Hotel . objects . filter ( id = id ) [0] )
		obj = MyUser . objects . get ( username = request . session ['username'])
		return render ( request , 'items.html', {'items' : items , 'status' : 'login', 'address' : obj . address, 'pno' : obj . phone_number})

	else : 

		return redirect ('login')

def placeorder ( request ) : 

	print ( request . GET )
	item_name = dict ( request . GET ) ['item_name']
	qt = dict ( request . GET ) ['qt']
	print ( request . POST )

	item_ids = json . dumps ( list ([ item_name, qt ]) )  
	print ( item_ids )
	obj = Order ( username = request . session ['username'] , hotel_id = request . session ['hotelid'], item_ids = item_ids , order_address = request . GET ['address'] + ' Contact : ' + request . GET [ 'pno'])
	# obj . gethoteladdress ()
	obj . save () 
	request . session ['order'] = { 'orderid' : obj . id  , 'username':request.session['username'], 'hotel_id' : request.session['hotelid'], 'item_ids' : eval(item_ids)}
	return redirect ('http://localhost:8000/orderstatus/' + str(obj . id) +'/')

def orderstatus ( request, id ) : 
	#print ( id )
	obj = Order . objects . get ( id = id )  #

	order = { 'orderid' : obj . id  , 'username':request.session['username'], 
	'hotel_id' : obj . hotel_id, 'item_ids' : eval(obj.item_ids)}
	print ( order )
	hotelName = Hotel . objects . filter ( id = order['hotel_id'] ) [0]

	itemsName = [ Item . objects . get ( id = x ) . item_name for x in order ['item_ids'] [0] ]
	itemsPrice = [ Item . objects . get ( id = x ) . item_price for x in order ['item_ids'] [0] ]
	itemdiscount=[ Item . objects . get ( id = x ) . item_discount for x in order ['item_ids'] [0] ]
	itemsQt = order ['item_ids'] [ 1 ]
	itemsQt = [ 0 if x == '' else x for x in itemsQt ]

	xorder = zip ( itemsName, itemsPrice,  itemdiscount, itemsQt  )
	price_after_discount = [ x - y for x , y in zip ( itemsPrice , itemdiscount )]
	print ( price_after_discount )
	total = sum ( [ int (x) * int(y) for x , y in zip ( itemsQt , price_after_discount )] ) 

	return render ( request , 'placeorder.html', {'order' : Order . objects.get ( id = id ) , 'hotel' : hotelName, \
		'itemsName' : itemsName, 'itemsPrice' : itemsPrice, 'itemdiscount':itemdiscount,'itemsQt' : itemsQt , 'xorder' : xorder,\
		'total' : total , 'status' : 'login' } )

def getorderstatus ( request , id  ) : 
	print ( request . GET , request . POST )

	obj = Order . objects . get ( id = id )
	print ( obj . id , obj . hotel_status)

	if obj . hotel_status != 'orderonhandofdelvboy' : 
		return JsonResponse ( {'status' : obj . hotel_status }) 
	else : 
		
		for x in  deliveryboy . objects . all (): 
			print ( 'Searching : ', x . name, x . id  )
			if obj in x . currentorder . all () : 
				status = x . __str__ () 
				break 
			else : 
				print ( 'Not found in : ', x . name , x . id )
		else : 
			status = 'Food is ready, searching fro deliveryboy!'
		return JsonResponse ( {'status' :  status }) 


def updateorderstatus ( request, hid , oid  ) : 

	print ( hid )
	print ( oid )
	print ( request . GET , request . POST )
	Order . objects . filter ( id = oid ) . update ( hotel_status = request . GET ['selected'])
	return redirect ( 'http://localhost:8000/hotels/{}/orders/' . format ( hid ))
