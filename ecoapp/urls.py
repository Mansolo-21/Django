from django.urls import path
from  .  import views
urlpatterns = [
    path('', views.index, name='index'),
    path('',views.about_us, name= 'about_us'),
    path('',views.services, name= 'services'),
    path('',views.contact_us, name= 'contact_us'),
    
]