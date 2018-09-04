from django import forms

class FindForm(forms.Form):
    widget_setting = forms.TextInput(attrs={'class': 'search-input'})
    find = forms.CharField(max_length=255, required=False, label="", widget=widget_setting)

class DetailForm(forms.Form):
    widget_setting = forms.TextInput(attrs={'class': 'detail-input'})
    release_widget = forms.TextInput(attrs={'class': 'detail-input','placeholder': '2018-09-04'})
    cd = forms.CharField(max_length=255, required=False, label="CD" ,widget=widget_setting)
    circle = forms.CharField(max_length=255, required=False, label="サークル" ,widget=widget_setting)
    song = forms.CharField(max_length=255, required=False, label="曲名" ,widget=widget_setting)
    vocal = forms.CharField(max_length=255, required=False, label="歌手" ,widget=widget_setting)
    lyric = forms.CharField(max_length=255, required=False, label="作詞" ,widget=widget_setting)
    arrange = forms.CharField(max_length=255, required=False, label="編曲" ,widget=widget_setting)
    ori_work = forms.CharField(max_length=255, required=False, label="原作" ,widget=widget_setting)
    ori_song = forms.CharField(max_length=255, required=False, label="原曲" ,widget=widget_setting)
    release = forms.CharField(max_length=255, required=False, label="発売日" ,widget=release_widget)