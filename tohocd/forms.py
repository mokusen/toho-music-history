from django import forms

class FindForm(forms.Form):
    widget_setting = forms.TextInput(attrs={'class': 'search-input'})
    find = forms.CharField(max_length=255, required=False, label="", widget=widget_setting)

class DetailForm(forms.Form):
    widget_setting = forms.TextInput(attrs={'class': 'detail-input'})
    circle = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    cd = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    song = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    vocal = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    lyric = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    arrange = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    ori_work = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    ori_song = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)
    release = forms.CharField(max_length=255, required=False, label="" ,widget=widget_setting)