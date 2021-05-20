import requests
import json

class DownloadCovidInfo:
    __url = ""
    def __init__(self, url = "https://api.covid19api.com/summary"):
        self.__url = url

    def get_all_data(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            print(response.status_code)
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Successfull Get Request')
            # response.content
            # response.text
            return response.json()
            
    def get_data_by_country(self, Country):
        for country in self.get_all_data()['Countries']:
            if Country.lower() == country['Country'].lower():
                return country

    def save_to_file(self, file):
        data = self.get_all_data()
        with open(''.join([file, '.json']), "w") as f:
            json.dump(data, f, indent=4)

    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url):
        self.__url = url

a = DownloadCovidInfo()

print(a.url)
print(a.get_all_data())
print(a.get_data_by_country('viet nam'))
a.save_to_file("CovidData")

