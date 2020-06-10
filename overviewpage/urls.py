from django.urls import path
from . import views

# . means from this directory, this file allows django to view webpages made in overviewpage's views.py
# views.home  access the home functions in views.py
urlpatterns = [
	path('', views.home, name='overviewpage-top'),
	path('about/', views.about, name='overviewpage-about'),
	path('links/', views.links, name='overviewpage-links'),
]
