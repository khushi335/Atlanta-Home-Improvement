from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('about/', about, name='about'),
    path('areas-we-serve/', areas_we_serve, name='areas_we_serve'),
    path('contact/', contact, name='contact'),
    
    # Services Group
    path('services/', services_home, name='services_home'), 
    path('bathroom-remodeling/', bathroom_remodeling, name='bathroom'),
    path('kitchen-remodeling/', kitchen_remodeling, name='kitchen'),
    path('basement-finishing/', basement_finishing, name='basement'),
    path('home-additions/', home_additions, name='additions'),
]
