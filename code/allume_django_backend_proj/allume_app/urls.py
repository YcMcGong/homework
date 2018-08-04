from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
    path('add_faq', views.add_faq, name = 'add_faq'),
    path('add_testimonial', views.add_testimonial, name = 'add_testimonial'),
    path('healthcheck', views.healthcheck, name = 'healthcheck'),
    path('index', views.index, name = 'index'), # only for the front-end homework testing on mobile
]