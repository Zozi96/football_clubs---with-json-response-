from django.db import models


class Country(models.Model):
    name = models.CharField(
        verbose_name='Nombre del pais',
        max_length=150,
        unique=True,
    )

    class Meta:
        db_table = 'pais'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(
        verbose_name='Nombre de la liga',
        max_length=200,
        unique='True',
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='leagues',
        verbose_name='Pais',
    )

    class Meta:
        db_table = 'liga'
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(
        verbose_name='Nombre del club',
        max_length=200,
        unique='True',
    )
    league = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
        related_name='clubs',
        verbose_name='Liga'
    )

    class Meta:
        db_table = 'club'
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name
