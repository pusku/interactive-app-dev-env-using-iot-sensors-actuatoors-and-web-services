from . import views
from .views import ActuatorListApiView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('actuators', views.ActuatorAPI)
router.register('sensors', views.SensorAPI)
router.register('service_registry', views.ServiceRegistryAPI)
router.register('mail_box', views.MailBoxAPI)
router.register('api', views.APInterfaceAPI)

urlpatterns = [
    path('', views.home, name='home_url'),
    path('api/', include(router.urls)),
    path('get_motor_status/', views.get_motor_status, name='status'),
    path('actuators/', ActuatorListApiView.as_view(), name="actuator_filter"),
]
