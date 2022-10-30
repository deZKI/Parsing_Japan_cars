import os
import bs4
import requests
from cars import MODELS
from cars import MARKERS

def start_search(marker, model, year, path, page=0):
    if marker not in MARKERS:
        return "Нет такой марки или ввели корректно, проверьте по сайту"
    if model not in MODELS[marker]:
        return "Нет такой модели или ввели корректно, проверьте по сайту"
    print(MODELS.keys())
    cars_urls = pagen_cars(MARKERS[marker], MODELS[marker][model], year, page)
    if len(cars_urls) == 0:
        return ('Пусто, таких тачек нет', f"https://kakaku.com/kuruma/used/spec/Maker={MARKERS[marker]}/Model={MODELS[marker][model]}/AgeType={year}/Page={page}")
    for i, car in enumerate(cars_urls):
        fullpath = os.path.join(path,car.split('/')[-2])
        os.mkdir(fullpath)
        print(i,":", car)
        download_photo(car, fullpath)
    return len(cars_urls)

def download_photo(url, fullpath):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    main = soup.find('ul', class_='thumbImgList').find_all('img')
    for i, photo in enumerate(main):
        if "https://movie1.goo-net.com/" in photo['src'] or "https://img1.kakaku.k-img.com" in photo['src']:
            continue
        response = requests.get(photo['src'])
        img = open(f'{fullpath}/img{i}.png', 'wb')
        img.write(response.content)
        img.close()
        print(photo['src'])



def pagen_cars(mark, models, age, pagen):  # можно генератор замутить
    # for i in models[1:]:
    #     fmodels = fmodels + ',' + str(i)
    url = f"https://kakaku.com/kuruma/used/spec/Maker={mark}/Model={models}/AgeType={age}/Page={pagen}"
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
