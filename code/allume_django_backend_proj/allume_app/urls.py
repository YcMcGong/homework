from . import views
from django.conf.urls import url, include

# Django 1.11.6
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^signin', views.signin, name = 'signin'),
    url(r'^signup', views.signup, name = 'signup'),
    url(r'^signout', views.signout, name = 'signout'),
    url(r'^add_faq', views.add_faq, name = 'add_faq'),
    url(r'^add_testimonial', views.add_testimonial, name = 'add_testimonial'),
    url(r'^healthcheck', views.healthcheck, name = 'healthcheck'),
    url(r'^index', views.index, name = 'index'), # only for the front-end homework testing on mobile
]


# Django 2.0
# from django.urls import path
# urlpatterns = [
#     path('', views.home, name = 'home'),
#     path('signin', views.signin, name = 'signin'),
#     path('signup', views.signup, name = 'signup'),
#     path('signout', views.signout, name = 'signout'),
#     path('add_faq', views.add_faq, name = 'add_faq'),
#     path('add_testimonial', views.add_testimonial, name = 'add_testimonial'),
#     path('healthcheck', views.healthcheck, name = 'healthcheck'),
#     path('index', views.index, name = 'index'), # only for the front-end homework testing on mobile
# ]