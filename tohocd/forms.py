from django import forms

class FindForm(forms.Form):
    find = forms.CharField(max_length=255, required=False)

class DetailForm(forms.Form):
    circle = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    cd = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    song = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    vocal = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    lyric = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    arrange = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    ori_work = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    ori_song = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))
    release = forms.CharField(max_length=255, required=False ,widget=forms.TextInput(
        attrs={'class': 'detail-input'}
    ))