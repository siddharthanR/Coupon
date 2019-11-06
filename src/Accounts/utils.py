import string 
import random 
from .models import Register
from django.http import Http404


# using random.choices() 
# generating random strings
def generator(): 
	return str(''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(7)))


#referal code validation of individual
def validate_referal_code(referalcode):
	#validating referalcode
	if referalcode is '':
		referalcode = generator()
	elif len(referalcode) == 7 and referalcode.isalnum():
		referalcode = referalcode
	else:
		raise Http404("length or alphanumeric problem")
	return referalcode


#referal code validation if user typed
def validate_referal_any(referalany):
	if len(referalany) == 7 and referalany.isalnum():
		try:
			code = Register.objects.get(referalcode = referalany)
		except Register.DoesNotExist:
			code = ''
			raise Http404("referal code is not available")
	return code


#email validation
def validate_email(email):
	qsemail = Register.objects.filter(email = email)
	if qsemail.exists():
		raise Http404('Email Already Exists')
	return email