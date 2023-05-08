from django.contrib import admin
from .models import Host, HostGroup
# Register your models here.

admin.site.register(Host)
admin.site.register(HostGroup)