from django.db import models


class Circle_master(models.Model):
    circle_name = models.CharField(max_length=255)
    circle_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Circle:id=' + str(self.id) + ',' + self.circle_name + '>'


class Cd(models.Model):
    circle = models.ForeignKey(Circle_master, on_delete=models.CASCADE)
    cd_name = models.CharField(max_length=255)
    cd_url = models.URLField(max_length=255, blank=True, null=True)
    release_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Cd:id=' + str(self.id) + ',' + self.cd_name + '>'


class Song(models.Model):
    cd = models.ForeignKey(Cd, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Song:id=' + str(self.id) + ',' + self.song_name + '>'


class Vocal_master(models.Model):
    vocal_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Vocal:id=' + str(self.id) + ',' + self.vocal_name + '>'


class Lyric_master(models.Model):
    lyric_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Lyric:id=' + str(self.id) + ',' + self.lyric_name + '>'


class Arrange_master(models.Model):
    arrange_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Arrange:id=' + str(self.id) + ',' + self.arrange_name + '>'


class Original_work_master(models.Model):
    original_work_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<OriWork:id=' + str(self.id) + ',' + self.original_work_name + '>'


class Original_song(models.Model):
    original_work = models.ForeignKey(Original_work_master, on_delete=models.CASCADE)
    original_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<OriSong:id=' + str(self.id) + ',' + self.original_name + '>'


class Song_info(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    vocal = models.ForeignKey(Vocal_master, on_delete=models.CASCADE, blank=True, null=True)
    lyric = models.ForeignKey(Lyric_master, on_delete=models.CASCADE, blank=True, null=True)
    arrange = models.ForeignKey(Arrange_master, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<SongInfo:id=' + str(self.id) + '>'


class Original_info(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    original_song = models.ForeignKey(Original_song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<OriInfo:id=' + str(self.id) + '>'
