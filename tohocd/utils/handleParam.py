from django.core.paginator import Paginator
from ..forms import FindForm
def create_param(model, num, any_dict):
    """
    画面へ渡すParamを設定する

    Parameters
    ----------
    model : models.any
        modelsモジュールのいずれかのクラス
    num : page number
        ページングのページナンバー
    any_dict : {any_name : any, ...}
        その他の設定要素
        any_name : anyを画面側で呼び出す際の名前
        any : 設定は各自で決定することが出来る  
    Returns
    -------
    param
        設定したParamを返す
    """
    max = len(model)
    display_min = 25 * (num - 1)
    display_max = 25 * num if num < max / 25 else max
    page = Paginator(model, 25)
    msg = "" if max != 0 else "検索した情報は存在しませんでした"
    param = {
        'data': page.get_page(num),
        'max': max,
        'msg': msg,
        'display_min': display_min,
        'display_max': display_max,
    }
    param.update(any_dict)
    return param

def __get_diff_param(request_value):
    """
    差分の辞書を形成し、返却する。

    Parameters
    ----------
    request_value : request.GET
        URLのParam
    
    Returns
    -------
    diff_param
        差分のParamを返す
    """

    check_list = ['song', 'cd', 'release', 'circle', 'vocal', 'lyric', 'arrange', 'ori_song', 'ori_work']
    check_set = set(check_list)
    param_list = [x for x in request_value]
    param_set = set(param_list)
    diff_list = check_set - param_set
    diff_param = {key: '' for key in diff_list}
    return diff_param

def check_param(request_value):
    """
    URLに対象となるParamが存在する
    存在する   -> pass
    存在しない -> ないParamを補填する

    Parameters
    ----------
    request_value : request.GET
        URLのParam
    
    Returns
    -------
    return_param
        補填したParamを返す
    """

    return_param = {key: value for key, value in request_value.items()}
    diff_param = __get_diff_param(request_value)
    return_param.update(diff_param)
    return return_param

def prepare_param(request_value):
    """
    request.GETから検索ワード、フォーム状態、ページナンバーを取得する

    Parameters
    ----------
    request_value : request.GET
        URLのParam
    
    Returns
    -------
    word : request.GET['find']
        検索ワード
    form : FindForm
        フォーム
    num : page number
        現在のページナンバー
    """

    if 'find' in request_value:
        word = request_value['find']
        form = FindForm(request_value)
    else:
        word = ""
        form = FindForm()
    num = prepare_param_page(request_value)
    return word, form, num

def prepare_param_page(request_value):
    """
    request.GETからページナンバーを取得する
    Parameters
    ----------
    request_value : request.GET
        URLのParam
    
    Returns
    -------
    num : page num
        現在のページナンバー
    """

    if 'page' in request_value:
        num = int(request_value['page'])
    else:
        num = 1
    return num

        