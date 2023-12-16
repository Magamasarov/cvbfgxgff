

from django.urls import path

from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('book/', views.book, name='book'),
     path('logout/', views.logout, name='logout'),


    
]
