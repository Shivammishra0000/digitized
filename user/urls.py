from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('event/',views.myevent),
    path('imagegallery/',views.igallery),
    path('videogallery/',views.vgallery),
    path('viewdetails/',views.viewdetails),
    path('booking/',views.booking),
    path('myticket/',views.myticket),
    path('myprofile/',views.myprofile),
    path('logout/',views.logout),

]

