from requests import Session
from bs4 import BeautifulSoup as BS
import re, json

req = Session()

class Dump:

    url = 'https://free.facebook.com'

    def __init__(self, cookies):
        self.__cookies = cookies
        self._id = []

    def __save(self, to):
        f = open('dump/'+to, 'w')
        f.write(json.dumps({
            'file_name': to,
            'data': self._id
        }))

    def from_friendlist(self, target='me'):
        self.__reset()
        if target == 'me':
            print('  (!) Mendapatkan ID dari Teman')
        else:
            r = req.get(self.url+'/'+target, cookies=self.__cookies).text
            nama = re.search(r'\<title\>(.*?)\<\/title\>', r).group(1)
            print('  (!) Mendapatkan ID dari '+nama)

        resp = req.get(self.url+'/'+target+'/friends?', cookies=self.__cookies)

        while True:
            print('\r  (!) Jumlah ID yang didapatkan: '+str(len(self._id)), flush=True, end='')
            pars = BS(resp.text, 'html.parser')
            tag_a = pars.find_all('a')

            for i in tag_a:
                try:
                    href = i['href']
                    if 'fref' in href:
                        if 'profile.php' in href:
                            r = re.search(r'id=(.*?)&', href).group(1)
                        else:
                            r = re.search(r'\/(.*?)\?', href).group(1)
                        self._id.append(r)
                except Exception as e:
                    print(e)
                    continue

            if 'Lihat Teman Lain' in resp.text:
                next_page = pars.find('a', string='Lihat Teman Lain')['href']
                resp = req.get(self.url+next_page, cookies=self.__cookies)
                continue
            else:
                break
        return self.__save(target)

    def from_reaction(self, post_url):
        post_url = post_url.replace('www', 'free')
        resp = req.get(post_url, cookies=self.__cookies)
        pars = BS(resp.text, 'html.parser')



    def __reset(self):
        self._id = []
