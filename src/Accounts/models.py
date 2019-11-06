from django.db import models

class Register(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField()
	email = models.EmailField(max_length = 50)
	city = models.CharField(max_length = 25)
	referalcode = models.CharField(max_length = 7, blank=True)
	referalany = models.CharField(max_length = 7, blank=True)

	def __str__(self):
		return self.referalcode

class Referal(models.Model):
	referal = models.ForeignKey(Register)
	myreferal = models.CharField(max_length = 7, null=True, blank=True)
	name = models.CharField(max_length = 120)
	email = models.EmailField(max_length = 100)   
	age = models.CharField(max_length = 10)
	city = models.CharField(max_length = 100)

	def __str__(self):
		return self.myreferal