from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.


class MusicAlbum(models.Model):
    title = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='album_author')

    def __str__(self):
        return f"'{self.title}' - {self.author}"


class Distribution(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Income(models.Model):

    MONTHS = (

        ('January','January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),

    )

    MONTHS2 = (

        (1,'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),

    )
    chanel = models.ForeignKey(Distribution, on_delete=models.CASCADE, related_name='distro_income')
    album = models.ForeignKey(MusicAlbum, on_delete=models.CASCADE, related_name='album_income')
    volume = models.FloatField()
    income = models.IntegerField(default=0)
    month = models.CharField(choices=MONTHS, default='January', max_length=64)
    month2 = models.IntegerField(choices=MONTHS2, default=1)
    year = models.IntegerField(default='2022')

    def __str__(self):
        return f"{self.chanel} {self.album} {self.income}"


class ArtistIncomeSpliter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inc_split')
    income_on = models.ForeignKey(Income, on_delete=models.CASCADE, related_name='inc_spliter')
    part_of_income = models.FloatField()

    def __str__(self):
        return f"{self.income_on} {self.part_of_income}"



class Storeroom(models.Model):
    TYPES = (
        ('CD','CD'),
        ('Vinyl','Vinyl'),
        ('Cassette','Cassette')
    )
    album = models.ForeignKey(MusicAlbum, on_delete=models.CASCADE, related_name='store_amount')
    carrier_type = models.CharField(choices=TYPES, max_length=64)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.carrier_type}"


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artist_message')
    text = models.TextField()

