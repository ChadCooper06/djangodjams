from django.db import models



class Artists(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.artists_text


class Albums(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.albums_text


class Songs(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    singer = models.ForeignKey(Artists, on_delete=models.CASCADE, blank=True, null=True)
    record = models.ForeignKey(Albums, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.songs_text


