__author__ = 'krishnasagar'

import requests
# from django.core.cache import cache


class MusicTrack:
    def __init__(self):
        self.baseUrl = 'http://104.197.128.152:8000/v1/tracks?page=%s'
        self.trackUrl = 'http://104.197.128.152:8000/v1/tracks/%s'
        self.url = 'http://104.197.128.152:8000/v1/tracks'

    def getMTracks(self, page=2):
        """
        Description : To fetch track list as per page numbers.
        Input Parameters :
            page : integer value representing page number.
        Output :
            result : object of track list, each iterable having title, rating, genres
        """
        r = requests.get(self.baseUrl % page)
        RJ = r.json()
        result = []
        if r.status_code == 200:
            if RJ['next'] is not None:
                result = RJ['results']
            else:
                result = {'End': RJ['results']}
        else:
            result = 'Error : status code %s' % r.status_code
        return result

    def getMTrack(self, id=None):
        """
        Description : To fetch track data as per track id
        Input Parameters :
            id : id value of track
        Output : json objectified result or error message on failure.
        """
        r = requests.get(self.trackUrl % id)
        if r.status_code == 200:
            return r.json()
        else:
            return 'Error : status code %s' % r.status_code

    def updateMTrack(self, id=None, data=None):
        """
        Description : To update track data as per track id
        Input Parameters :
            id : id value of track
        Output : json objectified result on success or error message on failure.
        """
        r = requests.post(self.trackUrl % id, data=data)
        if r.status_code == 200:
            return {'Success': r.json()}
        else:
            return {'Failure': 'Track record not updated %s' % r.status_code}

    def addMTrack(self, data=None):
        """
        Description : To add track data on server
        Input Parameters :
            data : jsonified data for posting on server
        Output : json objectified result on success or error message on failure.
        """
        r = requests.post(self.url, data=data)
        if r.status_code == 200:
            return {'Success': r.json()}
        else:
            return {'Failure': 'Track record' + r.json()['detail'].encode('ascii', 'ignore')}


class GenreTrack:
    def __init__(self):
        self.baseUrl = 'http://104.197.128.152:8000/v1/genres?page=%s'
        self.page = 2
        self.trackUrl = 'http://104.197.128.152:8000/v1/genres'

    def getGTracks(self):
        r = requests.get(self.baseUrl % self.page)
        RJ = r.json()
        result = []
        if r.status_code == 200:
            if RJ['next'] is not None:
                result = RJ['results']
                self.page += 1
            else:
                result = {'End': RJ['results']}
        else:
            result = 'Error : status code %s' % r.status_code
        return result

    def getGTPrevTracks(self):
        if self.page > 2:
            r = requests.get(self.baseUrl % (self.page - 2))
            self.page -= 1
        else:
            r = requests.get(self.trackUrl)
        RJ = r.json()
        result = []
        if r.status_code == 200:
            if RJ['previous'] is not None:
                result = RJ['results']
            else:
                result = {'Start': RJ['results']}
        else:
            result = 'Error : status code %s' % r.status_code
        return result

    def getGTAll(self):
        res = []
        r = requests.get(self.trackUrl)
        RJ = r.json()
        if r.status_code == 200:
            res += RJ['results']
        return res
        '''while(RJ['next'] != None):
            r = requests.get(RJ['next'])
            RJ = r.json()
            if r.status_code == 200:
                res += RJ['results']'''

    def getGTrack(self, id=None):
        r = requests.get(self.trackUrl + '/%s' % id)
        if r.status_code == 200:
            return r.json()
        else:
            return 'Error - getting genre record, status code %s' % r.status_code

    def updateGTrack(self, id=None, data=None):
        r = requests.post(self.trackUrl + '/%s' % id, data=data)
        if r.status_code == 200:
            return {'Success': r.json()}
        else:
            return {'Failure': 'Error for updating genre, status code %s' % r.status_code}

    def addGTrack(self, data=None):
        r = requests.post(self.trackUrl, data=data)
        if r.status_code == 200:
            return {'Success': r.json()}
        else:
            return {'Failure': 'Error for creating genre, status %s' % r.status_code}
