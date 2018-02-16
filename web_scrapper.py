import bs4
import requests


class Scrapper():

    def __init__(self, url, selector, name='Simple Scrapper'):
        self.name = name
        self.url = url
        self.selector = selector
        self.result = None

    def make_request(self):
        return requests.get(self.url)

    def get_scrapped_value(self):
        req = self.make_request()
        # Проверяем результат запроса на наличие страницы
        try:
            req.raise_for_status()
        except Exception as e:
            print("Не удалось сделать запрос - %s" % (e))
            return False

        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        value = soup.select(self.selector)[0].get_text()
        return value