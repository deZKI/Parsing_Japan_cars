import requests
import bs4
import xml

def get_markers():
    response = requests.get('https://kakaku.com/kuruma/used/spec/Maker=1/')
    soup = bs4.BeautifulSoup(response.content, 'lxml')

    selector = soup.find('div', class_='searchItem1Line')
    print()

    print(selector)
MARKERS = {
    "TOYOTA": 1,
    "LEXUS": 10,
    "NISSAN": 3,
    "HONDA": 2,
    "MAZDA": 5,
    "SUBARU": 6,
    "SUZUKI": 7,
    "DAIHATSU": 8,
}
