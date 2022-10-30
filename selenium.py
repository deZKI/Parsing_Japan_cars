from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

if __name__ == '__main__':
    url = 'https://stepik.org/'
    browser = webdriver.Chrome()
    browser.get(url)