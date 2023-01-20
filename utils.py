from requests import Session
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class Pars:
    def __init__(self, url: str):
        self.url: str = url
        self.session: Session = Session
        self.headers: dict = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': UserAgent().random
        }

    def get_response(self, url: str = None):
        if url is None:
            with self.session() as session:
                return session.get(url=self.url, headers=self.headers)
        with self.session() as session:
            return session.get(url=url, headers=self.headers)

    def get_urls(self, min_range: int = 1, max_range: int = 63):
        response = self.get_response()
        html_response = BeautifulSoup(response.content, 'lxml')
        cards = html_response.find('table', attrs={'class': 'article-table'}).find('tbody').find_all('tr')[1::]
        range_cards = len(cards)
        if 0 < min_range < max_range and min_range < max_range <= range_cards:
            for card in cards[min_range:max_range]:
                card = card.find_all('td')
                name, url, rarity = card[1].find('a').get('title'),\
                        'https://genshin-impact.fandom.com' + card[1].find('a').get('href'),\
                        card[2].find('img').get('title')
                yield name, url, rarity
        else:
            raise ValueError('Min and max values are not correct')

    def get_character(self, url: str, name: str, rarity: str):
        response = self.get_response(url=url)
        html_response = BeautifulSoup(response.content, 'lxml')

        if 'Nahida' == name:
            talant_cards = html_response.find_all('div', attrs={'class': 'card-container'})[145:154]
            evelation_cards = html_response.find_all('div', attrs={'class': 'card-container'})[29:39]
        else:
            talant_cards = html_response.find_all('div', attrs={'class': 'card-container'})[71:80]
            evelation_cards = html_response.find_all('div', attrs={'class': 'card-container'})[29:39]

        info = [[name, rarity]]

        evelation = []
        for card in evelation_cards:
            name = card.find('span', attrs={'class': 'card-caption'}).find('a').get('title').strip()
            count = card.find('span', attrs={'class': 'card-text card-font'}).text.strip().replace(',', '')
            evelation.append([name, int(count)])

        info.append(evelation)

        talants = []
        for card in talant_cards:
            name = card.find('span', attrs={'class': 'card-caption'}).find('a').get('title').strip()
            count = card.find('span', attrs={'class': 'card-text card-font'}).text.strip().replace(',', '')
            talants.append([name, int(count)])
        
        info.append(talants)

        return info


def main():
    p = Pars('https://genshin-impact.fandom.com/wiki/Character#Playable_Characters')
    for character in p.get_urls(min_range=25, max_range=40):
        if 'Traveler' not in character:
            print(p.get_character(url=character[1], name=character[0], rarity=character[2]))


if __name__ == '__main__':
    main()
