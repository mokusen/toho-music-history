from ..models import Circle_master
from django.db.models.functions import Lower


def get_circles(word):
    """
    あいまい検索でmodels.Circle_masterクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    circle
        models.Circle_masterクラスを返す
    """
    circle = Circle_master.objects.select_related().filter(circle_name__contains=word).order_by(Lower('circle_name'))
    return circle


def get_circle_byId(id):
    """
    models.Circle_master.idで完全一致検索を行い、Circle_masterクラスを取得する

    Parameters
    ----------
    id : int or str
        検索するID

    Returns
    -------
    circle
        models.Circle_masterクラスを返す
    """
    circle = Circle_master.objects.select_related().filter(id=id).order_by(Lower('circle_name'))
    return circle
