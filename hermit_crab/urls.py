from django.urls import path
from hermit_crab import views

urlpatterns = [
path('', views.index, name="index")
]
