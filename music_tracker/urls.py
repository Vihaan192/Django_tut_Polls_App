from django.urls import path
from . import views

app_name = "music_tracker"
urlpatterns = [
    path('', views.country_view, name='country'),
    path('search/', views.search_view, name='search'),
    path('similar/',views.similar_view, name = 'similar')
]