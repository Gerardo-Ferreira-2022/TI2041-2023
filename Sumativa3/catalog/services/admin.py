from django.contrib import admin
from .models import Provider, Service, Address, Contact

# Register your models here.
admin.site.register(Provider)
admin.site.register(Service)
admin.site.register(Address)
admin.site.register(Contact)