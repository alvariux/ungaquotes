from django.urls import path

from . import views

app_name = 'business'
urlpatterns = [
    path('', views.BusinessList.as_view(), name='list'),
    path('<int:pk>', views.BusinessDetail.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]