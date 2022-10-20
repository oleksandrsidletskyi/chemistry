from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('organic-spoluky', views.organic),
    path('izomery', views.izomery),
    path('alkany', views.alkany),
    path('alkeny', views.alkeny),
    path('alkiny', views.alkiny),
]

urlpatterns += staticfiles_urlpatterns()