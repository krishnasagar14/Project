from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import requests
from . import Music_Repo as MR
from .forms import TrackForm, GenreForm

MT = MR.MusicTrack()
GT = MR.GenreTrack()

addGenres = GT.getGTAll()

if type(addGenres) == str:
    print addGenres + "\n"


def Music_track(request, page=None):
    if type(addGenres) == str:
        return render(request, 'error.html', {'status': addGenres + " Reconnect internet and restart application"})
    if page is None:
        url = 'http://104.197.128.152:8000/v1/tracks'
        r = requests.get(url)
        if r.status_code == 200:
            RJ = r.json()
            next = RJ['next'].encode('ascii', 'ignore')
            return render(request, 'music_track.html', {'result': RJ['results'], 'nextUrl': next})
        return render(request, 'error.html', {'status': r.status_code})
    else:
        val = int(page)
        mt = MT.getMTracks(page=val)
        if type(mt) == str:
            return render(request, 'error.html', {'status': mt})
        if type(mt) == dict:
            return render(request, 'music_track.html', {'result': mt['End'], 'page_queue': [val - 2, val - 1, val]})
        else:
            return render(request, 'music_track.html', {'result': mt, 'page_queue': [val + 1, val + 2, val + 3]})


def Add_Track(request):
    if type(addGenres) == str:
        return render(request, 'error.html', {'status': addGenres + " Reconnect internet and restart application"})
    if request.method == 'POST':
        genres = str(request.POST['gname']).split(',')
        data = {'id': request.POST['id'].encode('ascii', 'ignore'), 'title': str(request.POST['tname']),
                'rating': request.POST['rating'].encode('ascii', 'ignore'), 'genres': genres}
        res = MT.addMTrack(data=data)
        if 'Success' in res:
            return render(request, 'error.html', res)
        if 'Failure' in res:
            return render(request, 'error.html', {'status': res['Failure']})
    else:
        t = []
        for i in addGenres:
            t.append((i['id'], i['name'].encode('ascii', 'ignore')))
        t = tuple(t)
        Tform = TrackForm(choices=t)
    return render(request, 'form1.html', {'form': Tform, 'next': 'addTrack'})


def Edit_Track(request, id=None):
    if type(addGenres) == str:
        return render(request, 'error.html', {'status': addGenres + " Reconnect internet and restart application"})
    if request.method == 'POST':
        genres = str(request.POST['gname']).split(',')
        data = {'id': request.POST['id'].encode('ascii', 'ignore'), 'title': str(request.POST['tname']),
                'rating': request.POST['rating'].encode('ascii', 'ignore'), 'genres': genres}
        res = MT.updateMTrack(id=data['id'], data=data)
        if 'Success' in res:
            return render(request, 'error.html', res)
        if 'Failure' in res:
            return render(request, 'error.html', {'status': res['Failure']})
    if id is not None:
        Tdict = MT.getMTrack(id)
        temp = {'tname': Tdict['title'].encode('ascii', 'ignore'), 'rating': Tdict['rating'].encode('ascii', 'ignore')}
        t = []
        if len(Tdict['genres']) > 0:
            for i in Tdict['genres']:
                t.append((i['id'], i['name'].encode('ascii', 'ignore')))
            for i in addGenres:
                t.append((i['id'], i['name'].encode('ascii', 'ignore')))
            t = tuple(t)
        else:
            for i in addGenres:
                t.append((i['id'], i['name'].encode('ascii', 'ignore')))
            t = tuple(t)  # ()
        EForm = TrackForm(data=temp, choices=t)
        return render(request, 'form1.html', {'form': EForm, 'id': id, 'next': 'editTrack'})


def Track_Genre(request, page=None):
    if type(addGenres) == str:
        return render(request, 'error.html', {'status': addGenres + " Reconnect internet and restart application"})
    if page is None:
        url = 'http://104.197.128.152:8000/v1/genres'
        r = requests.get(url)
        if r.status_code == 200:
            RJ = r.json()
            #next = RJ['next'].encode('ascii', 'ignore')
            return render(request, 'genre.html', {'result': RJ['results'], 'start': 1})
        return render(request, 'error.html', {'status': r.status_code})
    else:
        if int(page) == 1:
            mt = GT.getGTracks()
            if type(mt) == str:
                return render(request, 'error.html', {'status': mt})
            elif type(mt) == dict:
                return render(request, 'genre.html', {'result': mt['End'], 'end': 1})
            else:
                return render(request, 'genre.html', {'result': mt})
        elif int(page) == 0:
            mt = GT.getGTPrevTracks()
            if type(mt) == str:
                return render(request, 'error.html', {'status': mt})
            elif type(mt) == dict:
                return render(request, 'genre.html', {'result': mt['Start'], 'start': 1})
            else:
                return render(request, 'genre.html', {'result': mt})


def Add_Genre(request):
    if type(addGenres) == str:
        return render(request, 'error.html', {'status': addGenres + " Reconnect internet and restart application"})
    if request.method == 'POST':
        res = GT.addGTrack(data={'name': request.POST['gname'].encode('ascii', 'ignore')})
        if 'Success' in res:
            HttpResponse(res['Success'])
        else:
            HttpResponse(res['Failure'])
    Aform = GenreForm()
    return render(request, 'form2.html', {'id': id, 'form': Aform, 'next': 'addGenre'})


def Edit_Genre(request, id=None):
    if type(addGenres) == str:
        return render(request, 'error.html', {'status': addGenres + " Reconnect internet and restart application"})
    if request.method == 'POST':
        data = {'id': request.POST['id'].encode('ascii', 'ignore'),
                'name': request.POST['gname'].encode('ascii', 'ignore')}
        res = GT.updateGTrack(id=data['id'], data=data)
        if 'Success' in res:
            print 'Yes'
        if 'Failure' in res:
            print 'No'
    if id is not None:
        res = GT.getGTrack(id=id)
        if type(res) == str:
            return render(request, 'error.html', {'status': res})
        Eform = GenreForm(data={'gname': res['name']})
        return render(request, 'form2.html', {'id': id, 'form': Eform, 'next': 'editGenre'})