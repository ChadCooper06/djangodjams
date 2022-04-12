from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)
    singer = models.ForeignKey(Artist, on_delete=models.CASCADE)
    record = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


