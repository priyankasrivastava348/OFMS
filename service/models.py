from django.db import models
from datetime import datetime 
from random import randint 
# Create your models here.


class Hotel ( models . Model ) : 
	# id = models . CharField ( max_length = 20 , primary_key = True , default = randint ( 100000, 1000000 ))
	hotel_name = models . CharField ( max_length = 30 , unique=True, null = True , default = None )  
	hotel_address = models . CharField ( max_length = 100, null = True , default = None  ) 
	hotel_phone_number = models . CharField ( max_length = 20 ) 
	hotel_reting = models . IntegerField ( null = True , default = 0) 
	hoel_image = models . CharField ( max_length = 1000 , null = True , default = None )

	def __str__ ( self ) : 
		return self . hotel_name + ' '  + self . hotel_address 

class Item ( models . Model ) :

	hotel = models . ForeignKey( Hotel , on_delete=models.CASCADE, null = True , default = None )
	# hotel = models.OneToOneField( Hotel , to_field='hotel_name', on_delete=models.CASCADE)

	item_name = models . CharField ( max_length = 30  ) 
	item_price = models . IntegerField ( null = True , default = 0) 
	item_discount = models . IntegerField ( null = True , default = 0)
	item_image = models . CharField ( max_length = 1000 , null = True , default = None )
	def __str__ ( self ) : 

		return '{} \t {} \t {}' . format ( self . item_name, self . item_price, self . item_discount)

class  Order ( models . Model ) : 
	username = models . CharField ( max_length = 50 )
	hotel_id = models . CharField ( max_length = 20 )
	# hotel_address = models . CharField ( max_length = 100 , default = Hotel . objects . get ( id = hotel_id)) . hotel_address 
	item_ids = models . CharField ( max_length = 500 )
	order_date = models . DateField ( default = datetime . now  )
	hotel_status = models . CharField ( max_length = 30 ,default='Please Wait for Hotel conformation !', choices = [ [i,i] for i in  ['cancel', 'accept', 'processing', 'cooking', 'packed', 'delivered', 'orderonhandofdelvboy', 'On the Way', 'iod', 'Delivered']])
	order_address = models . CharField ( max_length = 500 , default = 'None', null = True )
	user_hotel_reting = models . IntegerField ( null = True )
	user_delivery_boy_reting = models . IntegerField ( null = True )  
	user_review = models . CharField ( max_length = 100 , null = True )
	
	def __str__ ( self ) : 

		return '{} {} {}'.format ( self . id , self . hotel_id , self.username , self . hotel_status )

	# def gethoteladdress ( self ) : 
	# 	obj = Hotel . objects . get( id =  self . hotel_id )
	# 	self . hoteladdress =  obj . hotel_name + ' '  + obj . hotel_address  