from django.urls import path
from . import views
urlpatterns = [
	path('list',views.view_list,name='viewlist'),
    path('', views.index,name='index'),
]
