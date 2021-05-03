from django.urls import path

from apps.club.views import LeaguesApiList, LeagueTemplate

app_name = 'club'

urlpatterns = [
    path('list/ligas/', LeagueTemplate.as_view(), name='list'),
    path('api/list/ligas/', LeaguesApiList.as_view(), name='api_list')
]
