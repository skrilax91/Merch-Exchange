from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
