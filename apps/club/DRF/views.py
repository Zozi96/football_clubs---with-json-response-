from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView, RetrieveUpdateAPIView,
)

from ..models import League, Country
from .serializers import LeagueSerializer, CountrySerializer


class LeaguesListAPIView(ListAPIView):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()


class CountryCreateAPIView(CreateAPIView):
    serializer_class = CountrySerializer


class LeaguesRetrieveAPIView(RetrieveAPIView):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()


class CountryDestroyAPIView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateAPIView(UpdateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CountryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
