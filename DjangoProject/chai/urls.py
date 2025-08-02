from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_index,name='all_index'),
    path('<int:chai_id>/',views.chai_details,name='chai_details'),
    path('chai_stores',views.Chai_store_view,name='chai_stores')
]
