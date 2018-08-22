from ..models import Original_song

def get_orisongs(word):
    """
    あいまい検索でmodels.Original_songクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    orisong
        models.Original_songクラスを返す
    """
    orisong = Original_song.objects.select_related().filter(original_name__contains=word).order_by('original_name')
    return orisong

def get_orisong_byId(id):
    """
    models.Original_song.idで完全一致検索を行い、Original_songクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するID
    
    Returns
    -------
    orisong
        models.Original_songクラスを返す
    """
    orisong = Original_song.objects.select_related().filter(id=id).order_by('original_name')
    return orisong
