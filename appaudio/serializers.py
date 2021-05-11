from rest_framework import serializers
from.models import Song,Podcast,AudioBook

class SongSerializers(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    Duration_of_seconds=serializers.CharField(required=False)
    class Meta:
        model= Song
        fields=['id','Name_of_song','Duration_of_seconds','Uploaded_time']

class PodcastSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    Duration_of_seconds = serializers.CharField(required=False)
    Host=serializers.CharField(required=False)
    Participants=serializers.CharField(required=False)
    class Meta:
        model= Podcast
        fields=['id','Name_of_Podcast','Duration_of_seconds','Uploaded_time','Host','Participants']



class AudioSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    Duration_of_seconds = serializers.CharField(required=False)
    Author_title=serializers.CharField(required=False)
    Narrator=serializers.CharField(required=False)
    class Meta:
        model= AudioBook
        fields=list_display = ['id','Title_audiobook','Author_title','Narrator','Duration_of_seconds' ,'Uploaded_time']