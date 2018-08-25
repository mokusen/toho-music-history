# タスク表
| タスク | 優先度 | 処理 | 日付 |
| :--- | :---: | :---: | :---: |
| tableの改行無効化 | 高 | 済 | 8/25 |
| ページングのCSS設定 | 高 | 済 | 8/25 |
| 歌手、作詞、編曲、原作の検索に対応 | 高 | 済 | 8/25 |
| 歌手、作詞、編曲、原作の件数表示設定 | 高 | 済 | 8/25 |
| 歌手、作詞、編曲、原作のForm設定追加(serviceの追加につながる) | 高 | 済 | 8/25 |
| indexページの作成 | 高 | 未 |  |
| Formの大きさ調整(detail以外) | 中 | 未 |  |
| search-wrapperの設定（両サイド少し幅を取る） | 中 | 未 |  |
| 各情報のul liのCSS変更(和風の青を使用する) | 低 | 未 |  |
| fontawesomeを使用した各題名のアイコン変更 | 低 | 未 |  |
| サークル、原作のアコーディオンのCSS設定（文字の色も含む） | 低 | 未 |  |
| ヘッダーのCSS変更（ロゴ、ハンバーガー） | 低 | 未 |  |
| mainのpタグ等のCSS変更 | 低 | 未 |  |
| htmlの文字サイズ変更、統一 | 低 | 未 |  |

# 拡張要素
| タスク | 実施 | 日付 |
| :--- | :---: | :---:|
| URL各種バリデーション | 未 |  |
| URL未定義の処理 | 済 | 8/25 |

# memo
~~~python
check_list = ['song', 'cd', 'release', 'circle', 'vocal', 'lyric', 'arrange', 'ori_song', 'ori_work']
    check_set = set(check_list)
    param_list = [x for x in request_value]
    param_set = set(param_list)
    print(f"param_set: {param_set}")
    diff_list = check_set - param_set
    print(f"diff_list: {diff_list}")
    return_param = {x:'' for x in diff_list}
    return_param.update(request_value)
~~~