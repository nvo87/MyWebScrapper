import bs4
import requests


class WebScrapper:
    def make_request(self, url):
        return requests.get(url)

    def get_new_value(self, url, selector):
        req = self.make_request(url)
        # Raising error if resource status is not 200
        req.raise_for_status()

        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        elements = soup.select(selector)
        if not elements:
            raise ElementNotFoundError('There is no such selectors')
        value = elements[0].get_text()

        return value


class ElementNotFoundError(Exception):
    pass
