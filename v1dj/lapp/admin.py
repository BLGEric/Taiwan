from django.contrib import admin
from lapp.models import Logindb,Newinfo

class lappadmin(admin.ModelAdmin):
	list_display = ('username','account','password')
admin.site.register(Logindb,lappadmin)

admin.site.register(Newinfo)
# Register your models here.
