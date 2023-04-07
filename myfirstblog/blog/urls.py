from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.result, name='result'),
    path('review/<int:pk>/', views.addComments, name='add_comments')



]
