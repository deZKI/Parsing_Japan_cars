import os
from tkinter import messagebox

import bs4
import requests
import threading

def start_search(marker, model="", year="", transmission="", drive="", fuel="", color="", steering="", page=1,
                 path=""):
    url = f"https://kakaku.com/kuruma/used/spec/Maker={marker}/Model={model}/AgeType={year}/Transmission={transmission}/Drive={drive}/Fuel={fuel}/Color={color}/Steering={steering}/Page={page}"
    cars_urls = pagen_cars(url)
    if len(cars_urls) == 0:
        msg = messagebox.showinfo("ОШИБКА", 'Пусто, таких тачек нет\n' + url)
    for i, car in enumerate(cars_urls):
        fullpath = os.path.join(path, car.split('/')[-2])
        try:
            os.mkdir(fullpath)
        except FileExistsError:
            a = threading.Thread(target=messagebox.showerror,args=('Ошибка', f'Машина была скачана{fullpath}'))
            a.start()
            continue
        print(i, ":", car)
        download_photo(car, fullpath)
    return len(cars_urls)


def download_photo(url, fullpath):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    # info = soup.find('div', 'itemBoxCell info c-box-regularBox')
    # print(info)
    lists = soup.find('div', class_='thumbImgArea').find_all('img')
    print(len(lists))
    for i, photo in enumerate(lists):
        print(i, photo['data-src'])
        if "https://movie1.goo-net.com/" in photo['data-src'] or "https://img1.kakaku.k-img.com" in photo['data-src']:
            continue
        response = requests.get(photo['data-src'])
        img = open(f'{fullpath}/img{i}.png', 'wb')
        img.write(response.content)
        img.close()


def pagen_cars(url):
    print(url)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    scroll = soup.findAll('div', class_='itemImgBox u-pRight15')
    l = []
    for i in scroll:
        f = "https://kakaku.com/" + i.contents[0]['href']
        print(f)
        l.append(f)
    return l
