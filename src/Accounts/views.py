from django.shortcuts import render, redirect
from .utils import validate_referal_code, validate_referal_any
from .forms import RegisterForm
from .models import Register, Referal

def registerUser(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form" : form,
		"title" : "User Registration"
	}
	if form.is_valid():
		name = form.cleaned_data.get('name')
		age = form.cleaned_data.get('age')
		email = form.cleaned_data.get('email')
		city = form.cleaned_data.get('city')
		referalcode = form.cleaned_data.get('referalcode')
		referalany = form.cleaned_data.get('referalany')
		
		#validating referal code of individual
		referalcode = validate_referal_code(referalcode)

		#validating referal code if user typed any
		newreferal = ''
		if referalany is not '':
			newreferal = validate_referal_any(referalany)
		else:
			referalany = ''

		if newreferal is '':
			#create an instance of register
			new_register = Register.objects.create(name=name,
				age=age,
				email=email,
				city=city,
				referalcode=referalcode,
				referalany=referalany)
			return render(request, 'list.html', {"title" : "User Registered Information",
				'obj' : new_register})

		else:
			new_register = Register.objects.create(name=name,
				age=age,
				email=email,
				city=city,
				referalcode=referalcode,
				referalany=referalany  )
			new_referal = Referal.objects.create(name=name,
				age=age,
				email=email,
				city=city,
				referal=newreferal,
				myreferal=referalcode  )
			return render(request, 'list.html', { "title" : "User Registered Information",
				'obj' : new_register})

	return render(request, "register.html", context)

def displayUser(request, name):
	obj = Register.objects.get(name=name)
	context = {
		'title' : 'User Registered Information',
		'obj' : obj,
	}
	render(request, 'list.html', obj)