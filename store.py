#!/usr/bin/python3
# coding=utf-8


•••••••••••••••••••••••••••••••••••••••
              go.py
  author: Yudhaha
  Ig    : https://instagram.com/yudamxr?igshid=oz075ik01ree
  fb    : https://www.facebook.com/damar.ky.16
  wa bot: Wa.me//+17145921008
•••••••••••••••••••••••••••••••••••••••

from datetime import datetime

class Store:

    passwordList = []
    passwordExtraList = []
    passwordLower = False
    instance = None

    def __init__(self):
        self.menu = {}
        self.object = {}
        self.login = None
        self.http = None
        self.brute = None

    def getDateTime(self):
        date = datetime.now().strftime('%d %B %Y')
        datetimes = datetime.now().strftime('%H:%M:%S')
        return '%s - %s'%(date, datetimes)

    def add(self, func = {}):
        num = '%02d'%((len(self.menu)+1),)
        self.menu[num] = {
            'name': '!m![!b!%s!m!] !p!%s' %(num, func['name']),
            'func': func['func'],
        }
        return self

    def generatePasswordFromName(self, name):
        data = []
        for pw in self.passwordExtraList:
            data.append(pw)
        name = name.strip().split(' ')
        for names in name[slice(0, 4)]:
            for num in self.passwordNameList:
                data.append(str(names+num).lower() if self.passwordLower else str(names+num))

        return data

    def setCredentials(self, data={}):
        self.object['credentials'] = data
        return self

    def setBaseURL(self, url):
        self.object['base'] = url
        return self

    def setLoginClass(self, clss):
        self.login = clss(self)
        return self

    def setHttpClass(self, clss):
        self.http = clss(self)
        return self

    def url(self, path=None):
        if path == None:
            return self.object['base'].format('/')
        else:
            return self.object['base'].format(path)