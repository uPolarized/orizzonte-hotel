# seu_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poll-data/', views.get_poll_data, name='poll_data'),
    path('poll-vote/', views.add_poll_vote, name='poll_vote'),
]