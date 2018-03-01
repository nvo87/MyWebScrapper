import pprint
import bs4
import requests

from dbconnect import UseDatabase

pp = pprint.PrettyPrinter(indent=4)


class Scrapper:
    """ Один скраппер, работа с его параметрами """

    def __init__(self, url: str, selector: str, name: str='Simple Scrapper'):
        self.id = None  # id в БД
        self.name = name
        self.url = url
        self.selector = selector
        self.result = None

    def __repr__(self) -> str:
        return str({
            'id': self.id,
            'name': self.name,
            'result': self.result,
        })

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


class ScrappersList:
    """ Список всех скрапперов и работа с этим списком """

    def __init__(self):
        self.all_scrappers = []

    def __repr__(self) -> list:
        return self.all_scrappers

    def get_all_scrappers(self) -> list:
        with UseDatabase() as cursor:
            SQL_select = """ SELECT * FROM scrappers """
            cursor.execute(SQL_select)
            scrappers_data = cursor.fetchall()

        for scrapper_data_item in scrappers_data:
            scrapper = Scrapper(name=scrapper_data_item[1],
                                url=scrapper_data_item[2],
                                selector=scrapper_data_item[3])
            scrapper.id = scrapper_data_item[0]
            scrapper.result = scrapper.get_scrapped_value()
            self.all_scrappers.append(scrapper)

        return self.all_scrappers

    def add_scrapper(self, name, url, selector) -> None:
        with UseDatabase() as cursor:
            SQL_insert = """ 
                            INSERT INTO scrappers 
                            (name, url, selector) 
                            VALUES (%s, %s, %s) 
                        """
            cursor.execute(SQL_insert, (name, url, selector, ))

    def del_scrapper(self, id) -> None:
        with UseDatabase() as cursor:
            SQL_delete = """ DELETE FROM scrappers
                            WHERE id = %s 
                        """
            cursor.execute(SQL_delete, (id,))
