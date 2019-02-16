from django.urls import path

from . import views

app_name = 'business'
urlpatterns = [
    path('', views.BusinessList.as_view(), name='list'),
    path('<int:pk>', views.BusinessDetail.as_view(), name='detail'),
    path('create', views.BusinessCreate.as_view(), name='create'),    
    path('update/<int:pk>', views.BusinessUpdate.as_view(), name='update'),
    path('detele/<int:pk>', views.BusinessDelete.as_view(), name='delete'),    
]