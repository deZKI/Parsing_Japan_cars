import bs4
import requests
import os


def start():
    path = '/Users/kirill201/Desktop/тест'
    cars_urls = pagen_cars(2, [30213], 2020)
    if len(cars_urls) == 0:
        print('Пусто, таких тачек нет')
        return
    for i, car in enumerate(cars_urls):
        fullpath = os.path.join(path, str(i))
        os.mkdir(fullpath)
        print(car)
        download_photo(car, fullpath)
def download_photo(url, fullpath):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    main = soup.find('ul', class_='thumbImgList').find_all('img')
    for i, photo in enumerate(main):
        response = requests.get(photo['src'])
        img = open(f'{fullpath}/img{i}.png', 'wb')
        img.write(response.content)
        img.close()
        print(photo['src'])



def pagen_cars(mark, models, age):  # можно генератор замутить
    fmodels = str(models[0])
    for i in models[1:]:
        fmodels = fmodels + ',' + str(i)
    url = f"https://kakaku.com/kuruma/used/spec/Maker={mark}/Model={fmodels}/AgeType={age}/"
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
