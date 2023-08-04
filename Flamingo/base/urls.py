from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerPage, name="register"),
    
    path('hair-type/',views.hairtype,name='hair-type'),
    path('skin-type/',views.skintype,name='skin-type'),
    path('nat-skin/',views.natskin,name='nat-skin'),
    path('nat-hair/',views.natskin,name='nat-hair'),
    path('art-nat/',views.artnat,name='art-nat'),


    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
