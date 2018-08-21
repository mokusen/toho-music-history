def create_param(song, num, any, any_name):
    """
    画面へ渡すParamを設定する

    Parameters
    ----------
    song : models.Song
        Songクラス
    num : page number
        ページングのページナンバー
    any : any
        設定は各自で決定することが出来る
    any_name : str
        anyを画面側で呼び出す際の名前
    
    Returns
    -------
    param
        設定したParamを返す
    """
    max = len(song)
    display_min = 25 * (num - 1)
    display_max = 25 * num if num >= max % 25 else max
    msg = "" if max != 0 else "検索した情報は存在しませんでした"
    param = {
        str(any_name): any,
        'data': song,
        'max': max,
        'msg': msg,
        'display_min': display_min,
        'display_max': display_max,
    }
    return param

def check_param(params):
    """
    URLに対象となるParamが存在する
    存在する   -> pass
    存在しない -> ないParamを補填する

    Parameters
    ----------
    params : request.GET
        URLのParam
    
    Returns
    -------
    return_param
        補填したParamを返す
    """

    check_list = ['song', 'cd', 'release', 'circle', 'vocal', 'lyric', 'arrange', 'ori_song', 'ori_work']
    check_set = set(check_list)
    param_list = [x[0] for x in params]
    param_set = set(param_list)
    diff_list = check_set - param_set
    return_param = {x:'' for x in diff_list}
    return return_param


        