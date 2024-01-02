from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:no>/',views.update,name="update"),
    path('delete/<int:no>/',views.delete,name="delete")
   
]