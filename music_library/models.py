from django.db import models

class Songs(models.Model):
    name = models.CharField(max_length=200)
    singer = models.ForeignKey(Artists)
    record = models.ForeignKey(Albums)


class Artists(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Albums(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artists)