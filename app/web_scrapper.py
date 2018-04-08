import bs4
import requests


class WebScrapper:
    def make_request(self, url):
        return requests.get(url)

    def get_new_value(self, url, selector):
        req = self.make_request(url)
        # Проверяем результат запроса на наличие страницы
        try:
            req.raise_for_status()
        except Exception as e:
            print("Не удалось сделать запрос - %s" % (e))
            return False

        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        try:
            value = soup.select(selector)[0].get_text()
        except Exception as e:
            print("Не удалось найти элемент - %s" % (e))
            return False

        return value
