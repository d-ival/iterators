import json
import requests

class CountriesWiki:
    wiki_common_url = 'https://en.wikipedia.org/wiki/'

    def __init__(self):
        url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
        response = requests.get(url)
        self.countries_list = list(json.loads(response.text))
        self.countries_iter = self.countries_list.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        country = next(self.countries_iter)
        common_name = str(country['name']['common'])

        wiki_country_url = self.wiki_common_url + common_name.replace(' ', '_')
        return (common_name, wiki_country_url)


with open('countries_wiki.txt', 'w', encoding='utf8') as file:
    for country_wiki in CountriesWiki():
        common_name = country_wiki[0]
        url = country_wiki[1]
        file.write(f'{common_name} - {url}\n')
