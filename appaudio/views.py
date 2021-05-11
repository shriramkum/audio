from django.shortcuts import render
from .serializers import SongSerializers,AudioSerializers,PodcastSerializers
from.models import Song,AudioBook,Podcast
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class SongSerializer(APIView):

    def get(self,request,pk):
        try:
            song=Song.objects.get(id=pk)
        except Song.DoesNotExist:
            message={"msg":"message is not created successfully"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer=SongSerializers(song)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def get_object_by_id(self,pk):
        try:
            song=Song.objects.get(id=pk)
        except Song.DoesNotExist:
            song=None
        return song
    def put(self,request,pk):
        song=self.get_object_by_id(pk)
        if song is None:
            message = {"msg": "Requested resource not available for Update"}
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer=SongSerializers(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object_by_id(pk)
        if song is None:
               message = {"msg": "Requested resource not available for Delete"}
               return Response(message, status=status.HTTP_404_NOT_FOUND)
        else:
            song.delete()
            song = {"msg": "Requested resource  Deleted successfully"}
            return Response(song, status=status.HTTP_204_NO_CONTENT)


class PodcastSerializer(APIView):
    def get(self,request,pk):
        try:
            podcast=Podcast.objects.get(id=pk)
        except Podcast.DoesNotExist:
            message={"msg":"message is not created successfully"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer=PodcastSerializers(podcast)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def get_object_by_id(self,pk):
        try:
            podcast=Podcast.objects.get(id=pk)
        except Podcast.DoesNotExist:
            podcast = None
        return podcast
    def put(self,request,pk):
        podcast=self.get_object_by_id(pk)
        if podcast is None:
            message={"msg":"requested podcast is not available in this."}
            return Response(message,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer=PodcastSerializers(podcast,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        podcast=self.get_object_by_id(pk)
        if podcast is None:
            message={"msg":"requested is not available in this podcast."}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        else:
            podcast.delete()
            message={"msg":"Data deleted is successfully...."}
            return Response(message,status=status.HTTP_204_NO_CONTENT)



class AudioBookSerializer(APIView):
    def get(self,request,pk):
        try:
            audio = AudioBook.objects.get(id=pk)
        except AudioBook.DoesNotExist:
            message={"msg":"message is not created successfully..."}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer=AudioSerializers(audio)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def get_object_pk_id(self,pk):
        try:
            audio=Podcast.objects.get(id=pk)
        except AudioBook.DoesNotExist:
            audio=None
        return audio
    def put(self,request,pk):
        audio=AudioBook.objects.get(pk)
        if audio is None:
            message={"msg":"requested data is not available in this audiobook..."}
            return Response(message,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer=AudioSerializers(audio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        audio=self.get_object_pk_id(pk)
        if audio is None:
            message={"msg":"requested is not available in this..."}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        else:
            audio.delete()
            message={"msg":"data is deleted sucessfully...."}
            return Response(message,status=status.HTTP_204_NO_CONTENT)

