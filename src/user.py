import requests as req
import re
import os

class User:

    url = 'https://free.facebook.com'

    def __init__(self):
        self.__cookies = None
        self.__username = None

    def login(self, cookies):
        cookie = {'cookies':cookies}
        resp = req.get(self.url+'/me', cookies=cookie).text
        if 'Buat Akun Baru' in resp:
            print('  (!) Cookies yang Anda masukan sudah tidak aktif.')
            if 'cookie' in os.listdir('.'):
                os.system('rm cookie')
            exit()
        elif 'Harap Konfirmasikan Identitas Anda' in resp:
            print('  (!) Akun Anda terkunci sementara/Checkpoint')
            exit()
        else:
            self.__cookies = cookie
            self.__username = re.search(r'\<title\>(.*?)\<\/title\>', resp).group(1)
            print('  (!) Login berhasil')
            # save cookie
            open('cookie', 'w').write(cookies)

    @property
    def cookie(self):
        return self.__cookies

    @property
    def username(self):
        return self.__username


if __name__ == '__main__':
    cookie = 'datr=nwppYMLsgqzHx1Aj_oKHAUyE;sb=nwppYOmeORWt9toC4DEEMb9h;dpr=2;locale=id_ID;fr=09IcR9UixHDpo3tLr.AWWyqcdAvpDW_wKZs2YfFrRHYh8.BgaIoT.8A.GCF.0.0.Bgh6cC.AWUaiAAeK2A;c_user=100043954149798;xs=27%3AWVUXp7_901-pRQ%3A2%3A1619502851%3A2927%3A10724;zsh=ASShyIdA9E2blP_E1hc-TICGuDYYj7e1LWHy91Uq0Zaj6p13C9SUad4p8XdioCuKi5OB4JXEugxLAMqP15xDBp0TC1DrTcxCeQKMHESp4tR91CN-atkMM8N7McUVdABIxw2iXoPXhO4OhIsmqJ4cT-P8NvWRy9-BAQeLmsoF4iIMcRJPgOlSZIGNem3lkD7gu4JWIZoJzp7JZEkROrP-GIOQO_PC5ytieCxGkSPSIJDxXRSe5V3wg4kB460Uoei-3otK0JOuQb01xlG4TKpbef_4CWKPQBBEktetzI3WLic5HWhchqHAcvirMW6YtG_u30_A8F4'
    user = User()
    print(user.login(cookie))
