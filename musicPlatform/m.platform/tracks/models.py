from django.db import models

# Create your models here.
class Album(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # Album id
    name = models.CharField(max_length=100)
    artist =  models.CharField(max_length=30)
    preview_url = models.URLField()
    img_url = models.URLField()
    tracks_number = models.IntegerField()
    release_date = models.CharField(max_length=30)

class Artist(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # Artist id
    name = models.CharField(max_length=100)
    genres = models.TextField()
    img_url = models.URLField()

class Features(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # track id
    artist_id =  models.CharField(max_length=30)
    album =  models.ForeignKey('Album', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tempo = models.FloatField()
    valence = models.FloatField()
    liveness = models.FloatField()
    instrumentalness = models.FloatField()
    acousticness = models.FloatField()
    speechiness = models.FloatField()
    mode = models.IntegerField()
    loudness = models.FloatField()
    energy = models.FloatField()
    danceability = models.FloatField()
    track_path = models.FilePathField(blank=True)
    sentiment  = models.CharField(max_length=30, blank=True)
    preview_url = models.URLField()

class UsersLike(models.Model):
    user = models.CharField(max_length=30) # user id
    track = models.CharField(max_length=30) # track id
    album = models.CharField(max_length=30) # album id

''' For Survey's tables  '''
class Survey20Tracks(models.Model):
    name = models.CharField(max_length=100)
    id =  models.CharField(max_length=30, primary_key=True) # track id
    artist_name = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=30)
    preview_url = models.URLField()

class SurveyResults(models.Model):
    # save the first time login survey content.
    user = models.CharField(max_length=30) # user id
    results = models.TextField() # dictionary format 
    date = models.DateTimeField()

class UserSurveyCompleted(models.Model):
    # save complete survey timestamp.
    user = models.CharField(max_length=30) # user id
    complete_date = models.DateTimeField()

''' For Recommender results ''' 
class RecSysResults(models.Model):
    user_id = models.CharField(max_length=30)
    album_img_url =  models.URLField()
    track_id = models.CharField(max_length=30)
    artist_name =  models.CharField(max_length=100)
    recom_method = models.CharField(max_length=2)
    '''
    Method: 
        0: Audio,
        1: Lyrics
        2: Hybrid
    '''
    recom_rank =  models.IntegerField()
    score = models.IntegerField(blank=True)
  
class RecFromRLResults(models.Model):
    user_id = models.CharField(max_length=30)
    album_img_url =  models.URLField()
    track_id = models.CharField(max_length=30)
    artist_name =  models.CharField(max_length=100)
    recom_rank =  models.IntegerField()
    score = models.IntegerField(blank=True)
    number_of_rec_times = models.IntegerField() 
