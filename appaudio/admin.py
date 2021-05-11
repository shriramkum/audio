from django.contrib import admin

from .models import Song,Podcast,AudioBook

class SongAdmin(admin.ModelAdmin):
    list_display = ['id','Name_of_song','Duration_of_seconds','Uploaded_time']
admin.site.register(Song,SongAdmin)


class PodcastAdmin(admin.ModelAdmin):
   list_display = ['id','Name_of_Podcast','Duration_of_seconds','Uploaded_time','Host','Participants']

admin.site.register(Podcast,PodcastAdmin)



class AudioAdmin(admin.ModelAdmin):
    list_display = ['id','Title_audiobook','Author_title','Narrator','Duration_of_seconds','Uploaded_time']

admin.site.register(AudioBook,AudioAdmin)

