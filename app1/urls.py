from django.urls import path
from . import views

urlpatterns = [
    path('url1',views.url1,name = 'url1'),
    path('url2',views.url,name = 'url'),
    
]