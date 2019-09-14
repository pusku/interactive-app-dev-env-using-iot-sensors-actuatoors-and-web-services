from . import views
from .views import ActuatorListApiView
from django.urls import path, include
from rest_framework import routers
from app_dir.main import app_creator, post_functions

# from app_dir.main import generated_functions

router = routers.DefaultRouter()
router.register('actuators', views.ActuatorAPI)
router.register('sensors', views.SensorAPI)
router.register('service_registry', views.ServiceRegistryAPI)
router.register('mail_box', views.MailBoxAPI)
router.register('api', views.APInterfaceAPI)
router.register('interactive', views.InteractiveAPI)

urlpatterns = [
    path('', views.home, name='home_url'),
    path('api/', include(router.urls)),
    path('Label/', post_functions.Label, name='Label'),
    path('recipe_puppy/', post_functions.recipe_puppy, name='recipe_puppy'),
    path('newspaper_headlines/', post_functions.newspaper_headlines, name='newspaper_headlines'),
    path('Read/', post_functions.Read, name='Read'),
    path('Search/', post_functions.Search, name='Search'),
    path('Send/', post_functions.Send, name='Send'),
    path('weather_info/', post_functions.weather_info, name='weather_info'),
    path('app_creator/', app_creator.create_app, name='app_creator'),
    path('eud_code/', views.eud_code, name='status'),
    path('actuators/', ActuatorListApiView.as_view(), name="actuator_filter"),

]
