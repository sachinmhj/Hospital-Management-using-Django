from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('records/', views.allrecords, name='records'),
    path('update/<int:iden>/', views.update, name='update'),
    path('delete/<int:pk>/', views.DeleteConfirm.as_view(), name='delete'),
    path('success/', views.success, name='success'),
]