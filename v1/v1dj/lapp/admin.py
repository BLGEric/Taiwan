from django.contrib import admin
from lapp.models import Logindb

class lappadmin(admin.ModelAdmin):
	list_display = ('username','account','password')
admin.site.register(Logindb,lappadmin)

# Register your models here.
