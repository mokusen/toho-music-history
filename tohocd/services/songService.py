from ..models import Song
from django.db.models import Q

def __check_param(param):
    """
    paramからorder_byのparamを決定する
    
    Parameters
    ----------
    param : request.GET['sort']
    
    Returns
    -------
    order_param : str
        order_byのparam
    sort_flag : asce or desc
        昇順、降順フラグ(元が昇順のとき、降順、降順の時、昇順を返す)
    """
    sort_flag = 'desc'
    if param == "song":
        order_param = 'song_name'
    elif param == "song_d":
        order_param = '-song_name'
        sort_flag = 'asce'
    elif param == "cd":
        order_param = 'cd__cd_name'
    elif param == "cd_d":
        order_param = '-cd__cd_name'
        sort_flag = 'asce'
    elif param == "release":
        order_param = 'cd__release_on'
    elif param == "release_d":
        order_param = '-cd__release_on'
        sort_flag = 'asce'
    elif param == "circle":
        order_param = 'cd__circle__circle_name'
    elif param == "circle_d":
        order_param = '-cd__circle__circle_name'
        sort_flag = 'asce'
    elif param == "vocal":
        order_param = 'song_info__vocal__vocal_name'
    elif param == "vocal_d":
        order_param = '-song_info__vocal__vocal_name'
        sort_flag = 'asce'
    elif param == "lyric":
        order_param = 'song_info__vocal__lyric_name'
    elif param == "lyric_d":
        order_param = '-song_info__vocal__lyric_name'
        sort_flag = 'asce'
    elif param == "arrange":
        order_param = 'song_info__vocal__arrange_name'
    elif param == "arrange_d":
        order_param = '-song_info__vocal__arrange_name'
        sort_flag = 'asce'
    elif param == "ori_song":
        order_param = 'original_info__original_song__original_name'
    elif param == "ori_song_d":
        order_param = '-original_info__original_song__original_name'
        sort_flag = 'asce'
    elif param == "ori_work":
        order_param = 'original_info__original_song__original_work__original_work_name'
    elif param == "ori_work_d":
        order_param = '-original_info__original_song__original_work__original_work_name'
        sort_flag = 'asce'
    else:
        order_param = 'pk'
    return order_param, sort_flag

def get_songs_byOR(word, param):
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
    sort_flag : asce or desc
        昇順、降順フラグ(元が昇順のとき、降順、降順の時、昇順を返す)
    """
    order_param, sort_flag = __check_param(param)
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
    ).order_by(order_param).distinct()
    return song, sort_flag

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

def get_song_byCd(id, param):
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
    order_param = __check_param(param)
    song = Song.objects.select_related().filter(cd__id=id).order_by(order_param)
    return song
    
def get_song_byVocal(id, word, param):
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
    order_param = __check_param(param)
    song = Song.objects.select_related().filter(
        Q(song_info__vocal__id=id),
        Q(song_name__contains=word) |
        Q(cd__cd_name__contains=word) |
        Q(cd__release_on__contains=word) |
        Q(cd__circle__circle_name__contains=word) |
        Q(song_info__vocal__vocal_name__contains=word) |
        Q(song_info__lyric__lyric_name__contains=word) |
        Q(song_info__arrange__arrange_name__contains=word) |
        Q(original_info__original_song__original_name__contains=word) |
        Q(original_info__original_song__original_work__original_work_name__contains=word)
        ).order_by(order_param)
    return song

def get_song_byLyric(id, word):
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
    order_param = __check_param(param)
    song = Song.objects.select_related().filter(
        Q(song_info__lyric__id=id),
        Q(song_name__contains=word) |
        Q(cd__cd_name__contains=word) |
        Q(cd__release_on__contains=word) |
        Q(cd__circle__circle_name__contains=word) |
        Q(song_info__vocal__vocal_name__contains=word) |
        Q(song_info__lyric__lyric_name__contains=word) |
        Q(song_info__arrange__arrange_name__contains=word) |
        Q(original_info__original_song__original_name__contains=word) |
        Q(original_info__original_song__original_work__original_work_name__contains=word)
        ).order_by(order_param)
    return song

def get_song_byArrange(id, word):
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
    order_param = __check_param(param)
    song = Song.objects.select_related().filter(
        Q(song_info__arrange__id=id),
        Q(song_name__contains=word) |
        Q(cd__cd_name__contains=word) |
        Q(cd__release_on__contains=word) |
        Q(cd__circle__circle_name__contains=word) |
        Q(song_info__vocal__vocal_name__contains=word) |
        Q(song_info__lyric__lyric_name__contains=word) |
        Q(song_info__arrange__arrange_name__contains=word) |
        Q(original_info__original_song__original_name__contains=word) |
        Q(original_info__original_song__original_work__original_work_name__contains=word)
        ).order_by(order_param)
    return song

def get_song_byOrisong(id, word):
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
    order_param = __check_param(param)
    song = Song.objects.select_related().filter(
        Q(original_info__original_song__id=id),
        Q(song_name__contains=word) |
        Q(cd__cd_name__contains=word) |
        Q(cd__release_on__contains=word) |
        Q(cd__circle__circle_name__contains=word) |
        Q(song_info__vocal__vocal_name__contains=word) |
        Q(song_info__lyric__lyric_name__contains=word) |
        Q(song_info__arrange__arrange_name__contains=word) |
        Q(original_info__original_song__original_name__contains=word) |
        Q(original_info__original_song__original_work__original_work_name__contains=word)
        ).order_by(order_param)
    return song