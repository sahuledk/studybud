from django.urls import path
from . import views

urlpatterns=[
path('athul/', views.athul, name = "athul"),
path('sag/', views.sag, name = "sag"),


]