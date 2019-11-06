from django.contrib import admin
from .models import Register, Referal

class RegisterAdmin(admin.ModelAdmin):
	list_display = ["name", "email", "city"]
	class Meta:
		model = Register

class ReferalAdmin(admin.ModelAdmin):
	list_display = ["referal", "name", "city"]
	class Meta:
		model = Referal		

admin.site.register(Referal, ReferalAdmin)
admin.site.register(Register, RegisterAdmin)