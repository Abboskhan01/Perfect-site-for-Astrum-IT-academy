from django.urls import path
from .views import home, meetings, meetings_details

urlpatterns = [
    path('', home, name='home_page'),
    path('meetings/', meetings, name='meetings_page'),
    path('meetings-details/', meetings_details, name='meetings_details_page'),

]