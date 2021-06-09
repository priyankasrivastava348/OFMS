from django.db import models
from service.models import Order

# Create your models here.
class deliveryboy (models.Model):
	name=models.CharField(max_length=10)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	location=models.CharField(max_length=30)
	phoneno=models.CharField(max_length=15)
	currentorder =  models.ManyToManyField(Order)
	status = models . CharField ( max_length= 30 ,  default = 'picked', null = True , choices = [ [i,i] for i in  ['picked', 'on the way', 'delivered' ]]  )
	rating = models . IntegerField ( default = 0 ) 

	def __str__ ( self ) : 
			return '''Delivery Boy Information :
Name : {}
Phone Number : {}
''' . format ( self . name , self . phoneno ) 