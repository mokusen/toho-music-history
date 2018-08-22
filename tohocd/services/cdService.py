from ..models import Cd
from django.db.models import Q

def get_cds(word):
    """
    あいまい検索でmodels.Cdクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    cd
        models.Cdクラスを返す
    """
    cd = Cd.objects.select_related().filter(
        Q(cd_name__contains=word) |
        Q(circle__circle_name__contains=word) |
        Q(release_on__contains=word)
    ).order_by('cd_name')
    return cd

def get_cd_byId(id):
    """
    models.Cd.idで完全一致検索を行い、Cdクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するID
    
    Returns
    -------
    cd
        models.Cdクラスを返す
    """
    cd = Cd.objects.select_related().filter(id=id).order_by('cd_name')
    return cd
