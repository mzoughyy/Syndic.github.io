from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="synd"),
    path('add_syndic',views.add_synd,name="add_synd")

]
