from ..models import Original_work_master
from django.db.models.functions import Lower


def get_oriworks(word):
    """
    あいまい検索でmodels.Original_work_masterクラスを取得する

    Parameters
    ----------
    word : int or str
        検索するワード

    Returns
    -------
    oriwork
        models.Original_work_masterクラスを返す
    """
    oriwork = Original_work_master.objects.select_related().filter(original_work_name__contains=word).order_by(Lower('original_work_name'))
    return oriwork


def get_oriwork_byId(id):
    """
    models.Original_work_master.idで完全一致検索を行い、Original_work_masterクラスを取得する

    Parameters
    ----------
    id : int or str
        検索するID

    Returns
    -------
    oriwork
        models.Original_work_masterクラスを返す
    """
    oriwork = Original_work_master.objects.select_related().filter(id=id).order_by(Lower('original_work_name'))
    return oriwork
