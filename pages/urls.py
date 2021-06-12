from django.urls import path

from .views import HomePageView, AboutPageView # new
from .views import House1PageView
from .views import House2PageView
from .views import House3PageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('house1/', House1PageView.as_view(), name='house1'),
    path('house2/', House2PageView.as_view(), name='house2'),
    path('house3/', House3PageView.as_view(), name='house3'),
]

