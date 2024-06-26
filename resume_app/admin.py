from django.contrib import admin
from .models import Roles,Location,Company,myuploadfile,addRoles,addLocation,addCompany
# Register your models here.
admin.site.register(Roles)
admin.site.register(Location)
admin.site.register(Company)
admin.site.register(myuploadfile)
admin.site.register(addRoles)
admin.site.register(addLocation)
admin.site.register(addCompany)

