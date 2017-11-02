from django.db import models

#album1 has primary key 1(unique Id)
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000) #album_logo will be linked to an URL, and Urls are quite big, so 1000
    
    #This function will print out the objects name on the database, or help filter out database results
    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  #Foreign key links to the primary key of Album
    song_title = models.CharField(max_length=500)
    file_type = models.CharField(max_length=10) #file extension
    
    def __str__(self):
        return self.song_title