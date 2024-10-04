from django.urls import path

from app.views import create_short_url, list_short_urls


app_name = 'app'
urlpatterns = [
    path('list_urls/', list_short_urls, name='list_urls'),
    path('get_short_urls/', create_short_url, name='short_urls')
]