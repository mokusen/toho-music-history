from ..models import Song
from django.db.models import Q

def get_songs(word):
    song = Song.objects.select_related().filter(
        Q(song_name__contains=word) |
        Q(cd__cd_name__contains=word) |
        Q(cd__release_on__contains=word) |
        Q(cd__circle__circle_name__contains=word) |
        Q(song_info__vocal__vocal_name__contains=word) |
        Q(song_info__lyric__lyric_name__contains=word) |
        Q(song_info__arrange__arrange_name__contains=word) |
        Q(original_info__original_song__original_name__contains=word) |
        Q(original_info__original_song__original_work__original_work_name__contains=word)
    ).order_by('pk').distinct()
    return song