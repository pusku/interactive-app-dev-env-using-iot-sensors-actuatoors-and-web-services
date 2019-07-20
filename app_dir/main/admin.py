from django.contrib import admin
from .models import Actuator, Sensor, ServiceRegistry, MailBox, API

admin.site.register(Actuator)
admin.site.register(Sensor)
admin.site.register(ServiceRegistry)
admin.site.register(MailBox)
admin.site.register(API)
