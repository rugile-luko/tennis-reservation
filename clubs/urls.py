from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('club/<club_pk>/<date>/', views.detail_view, name='detail_view'),
    path('reserve/<club_pk>/<date>/<court_pk>/<hour>/', views.reserve_court, name='reserve_court'),
    path('club/create/', views.create_club, name='create_club'),
    path('club/<club_pk>/court/<date>/', views.create_court, name='create_court'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('cancel-reservation/<reservation_pk>/', views.cancel_reservation, name='cancel_reservation')
]
