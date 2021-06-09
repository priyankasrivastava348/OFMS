from django.db import models
from datetime import datetime 
# Create your models here.

class MyUser  ( models . Model ) : 

	first_name = models . CharField ( max_length = 50 )
	last_name = models . CharField ( max_length = 30 )
	username = models . CharField ( max_length = 70 , primary_key = True )
	phone_number = models . CharField ( max_length = 20 , null = True , default = None )
	address = models . CharField (max_length = 500   ) 	
	password = models . CharField ( max_length = 20 )
	register_date = models . DateField ( default = datetime . now  )

	# def __init__ ( self ) : 
	# 	self . address = self . address + '\n' + self.phone_number