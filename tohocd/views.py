from django.shortcuts import render, redirect
from .forms import FindForm, DetailForm
from .services import songService, circleService, cdService, vocalService, lyricService, arrangeService, orisongService, oriworkService
from .utils import handleParam

def index(request):
    return render(request, 'tohocd/index.html')

def search(request):
    if 'find' in request.GET:
        word = request.GET['find']
        num = handleParam.prepare_param_page(request.GET)
        form = FindForm(request.GET)
        song = songService.get_songs_byOR(word)
        params = handleParam.create_param(song, num, {'form': form})
    else:
        form = FindForm()
        params = {"form":form, "max": 0}
    return render(request, 'tohocd/search.html', params)

def detail(request):
    if len(request.GET) != 0:
        word_dict = handleParam.check_param(request.GET)
        num = handleParam.prepare_param_page(request.GET)
        form = DetailForm(word_dict)
        song = songService.get_songs_byAND(word_dict)
        params = handleParam.create_param(song, num, {'form': form})
    else:
        form = DetailForm()
        params = {"form":form, "max": 0}
    return render(request, 'tohocd/detail.html', params)

def cd(request):
    word, form, num = handleParam.prepare_param(request.GET)
    cd = cdService.get_cds(word)
    params = handleParam.create_param(cd, num, {'form': form})
    return render(request, 'tohocd/cd.html', params)

def cd_redirect(request):
    return redirect('/tohocd/cd')

def cd_detail(request, id):
    cd = cdService.get_cd_byId(id)
    data = songService.get_song_byCd(id)
    params = {'cd': cd, 'data':data}
    return render(request, 'tohocd/cdDetail.html', params)

def circle(request):
    word, form, num = handleParam.prepare_param(request.GET)
    circle = circleService.get_circles(word)
    params = handleParam.create_param(circle, num, {'form': form})
    return render(request, 'tohocd/circle.html', params)

def vocal(request):
    word, form, num = handleParam.prepare_param(request.GET)
    vocal = vocalService.get_vocals(word)
    params = handleParam.create_param(vocal, num, {'form': form})
    return render(request, 'tohocd/vocal.html', params)

def vocal_redirect(request):
    return redirect('/tohocd/vocal')

def vocal_detail(request, id):
    word, form, num = handleParam.prepare_param(request.GET)
    vocal = vocalService.get_vocal_byId(id)
    data = songService.get_song_byVocal(id, word)
    params = handleParam.create_param(data, num, {'vocal': vocal, 'form': form})
    return render(request, 'tohocd/vocalDetail.html', params)

def lyric(request):
    word, form, num = handleParam.prepare_param(request.GET)
    lyric = lyricService.get_lyrics(word)
    params = handleParam.create_param(lyric, num, {'form': form})
    return render(request, 'tohocd/lyric.html', params)

def lyric_redirect(request):
    return redirect('/tohocd/lyric')

def lyric_detail(request, id):
    word, form, num = handleParam.prepare_param(request.GET)
    lyric = lyricService.get_lyric_byId(id)
    data = songService.get_song_byLyric(id, word)
    params = handleParam.create_param(data, num, {'lyric': lyric, 'form': form})
    return render(request, 'tohocd/lyricDetail.html', params)

def arrange(request):
    word, form, num = handleParam.prepare_param(request.GET)
    arrange = arrangeService.get_arranges(word)
    params = handleParam.create_param(arrange, num, {'form': form})
    return render(request, 'tohocd/arrange.html', params)

def arrange_redirect(request):
    return redirect('/tohocd/arrange')

def arrange_detail(request, id):
    word, form, num = handleParam.prepare_param(request.GET)
    arrange = arrangeService.get_arrange_byId(id)
    data = songService.get_song_byArrange(id, word)
    params = handleParam.create_param(data, num, {'arrange': arrange, 'form': form})
    return render(request, 'tohocd/arrangeDetail.html', params)

def orisong(request):
    word, form, num = handleParam.prepare_param(request.GET)
    orisong = orisongService.get_orisongs(word)
    params = handleParam.create_param(orisong, num, {'form': form})
    return render(request, 'tohocd/oriSong.html', params)

def orisong_redirect(request):
    return redirect('/tohocd/orisong')

def orisong_detail(request, id):
    word, form, num = handleParam.prepare_param(request.GET)
    orisong = orisongService.get_orisong_byId(id)
    data = songService.get_song_byOrisong(id, word)
    params = handleParam.create_param(data, num, {'orisong': orisong, 'form': form})
    return render(request, 'tohocd/oriSongDetail.html', params)

def oriwork(request):
    word, form, num = handleParam.prepare_param(request.GET)
    oriwork = oriworkService.get_oriworks(word)
    params = handleParam.create_param(oriwork, num, {'form': form})
    return render(request, 'tohocd/oriWork.html', params)
