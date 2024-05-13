"""Import modules for parsing"""
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


class PepperParser:
    """Class that parses pepper.ru"""


    def __init__(self):
        self.agent = UserAgent()
        self.headers = {'User-Agent': self.agent.chrome}
        self.url = "https://pepper.ru/"


    def parse(self):
        """Method that parses information and prints it"""
        page = requests.get(self.url , headers=self.headers, timeout = 10)
        soup = BeautifulSoup(page.text, "html.parser")
        actionslist = soup.find("div", {"class": "listLayout-main js-threadList"})

        for discount in actionslist:
            if discount.name == 'article':
                degree = discount.find("div", {"class": "threadGrid-headerMeta"})
                textitem = degree.find("span", {"class": "cept-vote-temp vote-temp vote-temp--hot"})
                if textitem is None:
                    continue
                degree_final = ' '.join(textitem.text.split()).replace('°','')
                name = discount.find("div", {"class": "threadGrid-title"})
                nametextitem = name.find("a", {"class": "cept-tt"})
                print("Акция: " + nametextitem.text)
                print("Градусов: " + degree_final)
                print("Ссылка: " + nametextitem['href'] + "\n")
