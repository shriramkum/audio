from django.db import models
from django.utils import timezone



class Entertainment(models.Model):
    id = models.IntegerField(primary_key=True)
    Duration_of_seconds = models.DurationField()
    Uploaded_time = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True

class Song(Entertainment):
    Name_of_song=models.FileField(upload_to='songs/' ,max_length=100)
    class Meta:
        verbose_name='Song'
        verbose_name_plural='Songs'

class Podcast(Entertainment):
    Name_of_Podcast=models.FileField(upload_to='podcast/',max_length=100)
    Host=models.CharField(max_length=100)
    Participants=models.CharField(max_length=100)
    class Meta:
        verbose_name='Podcast'
        verbose_name_plural='Podcasts'

class AudioBook(Entertainment):
    Title_audiobook=models.FileField(upload_to="audio/",max_length=100)
    Author_title=models.CharField(max_length=100)
    Narrator=models.CharField(max_length=100)
    class Meta:
        verbose_name='AudioBook'
        verbose_name_plural='AudioBooks'




