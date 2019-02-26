#!/usr/bin/python3

import os
import re
import sys
import urllib.request
from itertools import groupby

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""
def rabotaet():
    real_dir = os.getcwd()  # передаём дирректорию в которой сейчас находимся
    real_way = str(os.path.abspath(os.path.join(real_dir, 'apple-cat.ru_access.log')))
    ufile = urllib.request.urlopen('file:///' + real_way)
    html = ufile.read().decode('utf 8')
    some2 = re.findall(r'[0-9a-fA-F]{1,3}(?:[.][0-9a-fA-F]{1,3}){3}', html)
    some21 = list(set(some2))
    crt_index = open('index.html', 'w')
    style ="""{
box-shadow: 0 4px 8px 0 rgba(0,0,0,0.12),
            0 2px 4px 0 rgba(0,0,0,0.08);
}"""
    crt_index.write("""
<html>
<body>
<style>
h1 {6}
</style>
<h1>
  <h1>  {0:5} </h1> 
  <h1>  {1} </h1>   
    <h1>  {2} </h1>
    <h1>  {3} </h1> 
    <h1>  {4} </h1>  
    <h1>  {5} </h1> 
</h1>
</body>
</html>""".format(some21[0], some21[1], some21[2], some21[3], some21[4], some21[5], style))

def read_urls(filename):

    return []
  

def download_images(img_urls, dest_dir):

    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает директорию, если это необходимо.
    """
    # +++ваш код+++
  

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
