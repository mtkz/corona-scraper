import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"
country = []
cases = []


class Helper:

    def __init__(self):
        print('connected !')

    def data_getter(self, url):
        virus_data = requests.get(url)
        return virus_data

    def data_miner(self, pageContent):
        data_soup = BeautifulSoup(pageContent, 'html.parser')

        tbody = data_soup.find('tbody')

        all_tr = tbody.findAll('tr')

        return all_tr

    def data_writer(self, rows):
        with open('coronaDataSet.txt', 'w') as f:

            for row in rows:

                datas = row.text.replace('\n', ' ').split(" ")

                for data in datas:
                    f.write(data + " ")

                f.write('\n')

    def data_printer(self):
        row = 1
        file = open('coronaDataSet.txt', 'r')
        for slc in enumerate(file):

            if slc[0] in (0, 1, 2, 3, 4, 5, 6, 7):
                continue

            country.append(slc[1].split(" ")[1])
            try:
                cases.append(int(slc[1].split(" ")[2]))
            except:
                pass
            row += 1

        file.close()

    def show_chart(self):
        plt.bar(country[0:10],  cases[0:10])
        plt.savefig('corona.png')


helper = Helper()

pageContect = helper.data_getter(URL)
rows = helper.data_miner(pageContect.content)
helper.data_writer(rows=rows)
helper.data_printer()
helper.show_chart()
