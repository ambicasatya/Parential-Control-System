from django.urls import path,include
from . import views
urlpatterns=[path('',views.home,name='home'),
             path('generate',views.generate,name='generate'),
             path('delete_from_dropbox',views.delete_from_dropbox,name='delete_from_dropbox'),
            ]