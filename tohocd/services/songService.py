from ..models import Song
from django.db.models import Q
from django.db.models.functions import Lower

def __check_param(param):
    """
    paramからorder_byのparamを決定する
    
    Parameters
    ----------
    param : request.GET['sort']
    
    Returns
    -------
    order_param : Lower(str)
        order_byのparam(小文字)
    """
    param_dict = {
        "song": "song_name",
        "song_d": "song_name",
        "cd": "cd__cd_name",
        "cd_d": "cd__cd_name",
        "release": "cd__release_on",
        "release_d": "cd__release_on",
        "circle": "cd__circle__circle_name",
        "circle_d": "cd__circle__circle_name",
        "vocal": "song_info__vocal__vocal_name",
        "vocal_d": "song_info__vocal__vocal_name",
        "lyric": "song_info__lyric__lyric_name",
        "lyric_d": "song_info__lyric__lyric_name",
        "arrange": "song_info__arrange__arrange_name",
        "arrange_d": "song_info__arrange__arrange_name",
        "ori_song": "original_info__original_song__original_name",
        "ori_song_d": "original_info__original_song__original_name",
        "ori_work": "original_info__original_song__original_work__original_work_name",
        "ori_work_d": "original_info__original_song__original_work__original_work_name",
    }
    if param in param_dict:
        if "release" in param:
            order_param = param_dict[param]
        else:
            order_param = Lower(param_dict[param])
    else:
        order_param = "pk"
    return order_param

def __reverse(song, param, order_param):
    """
    reverseを行うメソッド

    Parameters
    ----------
    song : models.Songクラス

    param : request.GET['sort]

    order_param : str
    
    Returns
    -------
    song : models.Song.reverse()
    """

    if order_param != "pk" and "_d" in param:
        song = song.reverse()
    return song

def get_songs_byOR(word, param):
    """
    曖昧OR検索でmodels.Songクラスを取得する

    Parameters
    ----------
    word : search_word
        検索するワード
    param : request.GET['sort]
        リクエストのsortパラメーター
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    order_param = __check_param(param)
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
    song = __reverse(song, param, order_param)
    return song

def get_songs_byAND(word_dict, param):
    """
    曖昧AND条件でmodels.Songクラスを取得する
    
    Parameters
    ----------
    word_dict : search_dict
        song,cd,release,circle,vocal,lyric,arrange,ori_song,ori_workを所持した辞書
    param : request.GET['sort]
        リクエストのsortパラメーター
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    order_param = __check_param(param)
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
    ).order_by(order_param).distinct()
    song = __reverse(song, param, order_param)
    return song

def get_song_byCd(id, param):
    """
    models.Cd.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    param : request.GET['sort]
        リクエストのsortパラメーター
    
    Returns
    -------
    song
        models.Songクラスを返す
    """
    order_param = __check_param(param)
    song = Song.objects.select_related().filter(cd__id=id).order_by(order_param)
    song = __reverse(song, param, order_param)
    return song
    
def get_song_byVocal(id, word, param):
    """
    models.Vocal_master.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    param : request.GET['sort]
        リクエストのsortパラメーター
    
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
        ).order_by(order_param).distinct()
    song = __reverse(song, param, order_param)
    return song

def get_song_byLyric(id, word, param):
    """
    models.Lyric_master.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    param : request.GET['sort]
        リクエストのsortパラメーター
    
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
        ).order_by(order_param).distinct()
    song = __reverse(song, param, order_param)
    return song

def get_song_byArrange(id, word, param):
    """
    models.Arrange_master.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    param : request.GET['sort]
        リクエストのsortパラメーター
    
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
        ).order_by(order_param).distinct()
    song = __reverse(song, param, order_param)
    return song

def get_song_byOrisong(id, word, param):
    """
    models.Original_song.idの完全一致でmodels.Songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するCDのID
    param : request.GET['sort]
        リクエストのsortパラメーター
    
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
        ).order_by(order_param).distinct()
    song = __reverse(song, param, order_param)
    return song