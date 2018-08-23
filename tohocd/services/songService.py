from ..models import Song
from django.db.models import Q

def get_songs_byOR(word):
    """
    曖昧OR検索でmodels.Songクラスを取得する

    Parameters
    ----------
    word : search_word
        検索するワード
    
    Returns
    -------
    song
        models.Songクラスを返す
    """

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

def get_songs_byAND(word_dict):
    """
    曖昧AND条件でmodels.Songクラスを取得する
    
    Parameters
    ----------
    word_dict : search_dict
        song,cd,release,circle,vocal,lyric,arrange,ori_song,ori_workを所持した辞書
    
    Returns
    -------
    song
        models.Songクラスを返す
    """

    song = Song.objects.select_related().filter(
        Q(song_name__contains=word_dict['song']),
        Q(cd__cd_name__contains=word_dict['cd']),
        Q(cd__release_on__contains=word_dict['release']),
        Q(cd__circle__circle_name__contains=word_dict['circle']),
        Q(song_info__vocal__vocal_name__contains=word_dict['vocal']),
        Q(song_info__lyric__lyric_name__contains=word_dict['lyric']),
        Q(song_info__arrange__arrange_name__contains=word_dict['arrange']),
        Q(original_info__original_song__original_name__contains=word_dict['ori_song']),
        Q(original_info__original_song__original_work__original_work_name__contains=word_dict['ori_work'])
    ).order_by('pk').distinct()
    return song

def get_song_byCd(id):
    """
    models.Cd.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    song = Song.objects.select_related().filter(cd__id=id).order_by('pk')
    return song
    
def get_song_byVocal(id):
    """
    models.Vocal_master.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    song = Song.objects.select_related().filter(song_info__vocal__id=id).order_by('pk')
    return song

def get_song_byLyric(id):
    """
    models.Lyric_master.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    song = Song.objects.select_related().filter(song_info__lyric__id=id).order_by('pk')
    return song

def get_song_byArrange(id):
    """
    models.Arrange_master.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    song = Song.objects.select_related().filter(song_info__arrange__id=id).order_by('pk')
    return song

def get_song_byOrisong(id):
    """
    models.Original_song.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    song = Song.objects.select_related().filter(original_info__original_song__id=id).order_by('pk')
    return song