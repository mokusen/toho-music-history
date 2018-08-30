from ..models import Arrange_master
from django.db.models.functions import Lower

def get_arranges(word):
    """
    あいまい検索でmodels.Arrange_masterクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    arrange
        models.Arrange_masterクラスを返す
    """
    arrange = Arrange_master.objects.select_related().filter(arrange_name__contains=word).order_by(Lower('arrange_name'))
    return arrange

def get_arrange_byId(id):
    """
    models.Arrange_master.idで完全一致検索を行い、Arrange_masterクラスを取得する
    
    Parameters
    ----------
    id : int or str
        検索するID
    
    Returns
    -------
    arrange
        models.Arrange_masterクラスを返す
    """
    arrange = Arrange_master.objects.select_related().filter(id=id).order_by(Lower('arrange_name'))
    return arrange
