#!/usr/bin/python3
# coding=utf-8

•••••••••••••••••••••••••••••••••••••••
              go.py
  author: Yudhaha
  Ig    : https://instagram.com/yudamxr?igshid=oz075ik01ree
  fb    : https://www.facebook.com/damar.ky.16
  wa bot: Wa.me//+17145921008
•••••••••••••••••••••••••••••••••••••••

import os, glob, re, json
from src.CLI import (prints, br, progressBar, banner)

listDIR = ['session','crack', 'result']

for dir in listDIR:
    try:
        os.mkdir(dir)
    except: pass

def sessionList():
    data = []
    for file in glob.glob('session/*.json'):
        try:
            read = open(file, 'r', encoding='utf-8').read()
            load = json.loads(read)
            data.append(load)
        except: pass

    return data

def cacheDumpList():
    data = []
    for file in glob.glob('crack/*.json'):
        try:
            size = os.path.getsize(file)
            read = open(file, 'r', encoding='utf-8').read()
            load = json.loads(read)
            name = '%s (%s) size bytess: %s' %(load['file_name'], load['created_at'], size)
            data.append({'name': name, 'path': file})
        except: pass

    return data

def resultCrack(dir='result', name=''):
    if os.path.exists('%s/%s.json'%(dir, name)) == False:
        return []
    try:
        read = open('%s/%s.json'%(dir, name), 'r', encoding='utf-8').read()
        load = json.loads(read)
        return load['data']
    except:
        return []

def isActive(self):
    cookies = readCookies()
    progressBar(text='Mengecek cookies...', max=25)
    self.store.http.setCookies(cookies)
    id = re.findall(r'c_user=(\d+);', cookies)[0]
    try:
        response = self.store.http.get('/profile').text()
        name = self.store.http.currentTitle()
    except:
        br(1)
        prints('!m!Tidak ada koneksi mohon cek koneksi internet Anda.!r!', blank_left=4)
        exit()
    if 'mbasic_logout_button' in str(response):
        banner()
        if 'Laporkan Masalah' not in str(response):
            try:
                http = self.store.http.get('/language.php')
                for i in http.bs4().find_all('a'):
                    if 'Bahasa Indonesia' in str(i):
                        http.get(i['href'])
            except: pass
        self.store.setCredentials({
            'id': id,
            'name': name
        })
        return True
    else:
        try:
            os.remove('.login.json')
            os.remove('session/%s.json'%(id))
        except:
            pass
        return False

def isLogin():
    cookies = readCookies()
    if cookies == '':
        return False
    else:
        return True

def readCookies():
    try:
        read = open('.login.json', 'r', encoding='utf-8').read()
        load = json.loads(read)
        return load['credentials']['cookies']
    except:
        return ''