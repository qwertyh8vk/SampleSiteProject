from django.urls import path
from . import views

urlpatterns = [
    path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric'),
    path('', views.main_page, name='home'),
    path('bboard/', views.home_page, name='home'),
]