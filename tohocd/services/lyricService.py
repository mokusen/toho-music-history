from ..models import Lyric_master
from django.db.models.functions import Lower


def get_lyrics(word):
    """
    あいまい検索でmodels.Lyric_masterクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    lyric
        models.Lyric_masterクラスを返す
    """
    lyric = Lyric_master.objects.select_related().filter(lyric_name__contains=word).order_by(Lower('lyric_name'))
    return lyric


def get_lyric_byId(id):
    """
    models.Lyric_master.idで完全一致検索を行い、Lyric_masterクラスを取得する

    Parameters
    ----------
    id : int or str
        検索するID

    Returns
    -------
    lyric
        models.Lyric_masterクラスを返す
    """
    lyric = Lyric_master.objects.select_related().filter(id=id).order_by(Lower('lyric_name'))
    return lyric
