from django.urls import path

from apps.club.generic.views import LeaguesApiList, LeagueTemplate
from apps.club.DRF.views import (
    LeaguesListAPIView,
    CountryCreateAPIView,
    LeaguesRetrieveAPIView,
    CountryDestroyAPIView, CountryUpdateAPIView, CountryRetrieveUpdateAPIView
)

app_name = 'club'

urlpatterns = [
    path('list/ligas/', LeagueTemplate.as_view(), name='list'),
    path('api/list/ligas/', LeaguesApiList.as_view(), name='api_list')
]

api_urls = [
    path('rest/list/ligas/', LeaguesListAPIView.as_view(), name='rest_list_league'),
    path('rest/<int:pk>/detail/liga/', LeaguesRetrieveAPIView.as_view(), name='rest_retrieve_league'),
    path('rest/create/pais/', CountryCreateAPIView.as_view(), name='rest_create_country'),
    path('rest/<int:pk>/destroy/pais/', CountryDestroyAPIView.as_view(), name='rest_delete_country'),
    path('rest/<int:pk>/update/pais/', CountryUpdateAPIView.as_view(), name='rest_update_country'),
    path('rest/<int:pk>/modify/pais/', CountryRetrieveUpdateAPIView.as_view(), name='rest_modify_country'),
]

urlpatterns += api_urls
