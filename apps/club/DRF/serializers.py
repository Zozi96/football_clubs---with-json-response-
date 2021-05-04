from rest_framework import serializers

from ..models import League, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    # Backward relationship (Related name)
    clubs = serializers.StringRelatedField(many=True)
    # Foreign Key
    country = CountrySerializer()

    class Meta:
        model = League
        fields = (
            'id',
            'name',
            'country',
            'clubs',
        )
