class SongFeatures(models.Model):
    id = models.CharField(max_length=30, primary_key=True) # track id
    name = models.CharField(max_length=100)
    audio_features = models.TextField()
    lyrics_features = models.TextField()