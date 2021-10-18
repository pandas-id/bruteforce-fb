'''
date: 16 juli 2021
lastdate: 2021-09-16
'''

from os import get_terminal_size

# color
n = '\033[0m'  # normal
r = '\033[91m' # red
g = '\033[92m' # green
y = '\033[93m' # yellow
c = '\033[94m' # cyan

def prints(text, tabs=2, middle=False) -> str:
    """
    n: normal, r: red, g: green, y: yellow, c: cyan
    """
    # coloring
    text = text.replace('<n>', n)
    text = text.replace('<r>', r)
    text = text.replace('<g>', g)
    text = text.replace('<y>', y)
    text = text.replace('<c>', c)
    text = text+n

    if middle:
        ctr = get_terminal_size().columns
        return print(text.center(ctr))

    return print(' '*tabs+text)

if __name__ == '__main__':
    prints(f'<h>Akmal')
    # prints('<m>Akmal')
    # prints('<h>Akmal')
    # prints('<k>Akmal')
    # prints('<c>Akmal')
