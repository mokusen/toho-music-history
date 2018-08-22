from ..models import Vocal_master

def get_vocals(word):
    """
    あいまい検索でmodels.Vocal_masterクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    vocal
        models.Vocal_masterクラスを返す
    """
    vocal = Vocal_master.objects.select_related().filter(vocal_name__contains=word).order_by('vocal_name')
    return vocal

def get_vocal_byId(id):
    """
    models.Vocal_master.idで完全一致検索を行い、Vocal_masterクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するID
    
    Returns
    -------
    vocal
        models.Vocal_masterクラスを返す
    """
    vocal = Vocal_master.objects.select_related().filter(id=id).order_by('vocal_name')
    return vocal
