import os
import sys
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Scraper:
    def __init__(self, webtable):
        self.table = webtable

    def getLinksList(self, column_number=10):
        sys.stdout.write(
            '\r'+'Scanning Complete.\nPreparing Links For Download...\n')
        linksColumn = self.table.find_elements_by_xpath(
            "//tr/td["+str(column_number)+"]/a")
        LinksList = []
        for webElement in linksColumn:
            LinksList.append(webElement.get_attribute('href'))

        sys.stdout.write('\r'+'Links Prepared.\n')
        return LinksList

    def getDownloadLinks(self):
        sys.stdout.write('\r'+'Fetching Download Links.\n')
        downloadLinks = []
        for eachLink in self.getLinksList():
            driver.get(eachLink)
            dl = driver.find_element_by_xpath("//*[@id='info']/h2/a")
            downloadLinks.append(dl.get_attribute('href'))
        self.writeDownloadLinksToFile(downloadLinks)

    def writeDownloadLinksToFile(self, downloadLinks):
        sys.stdout.write('\r'+'Writing Download Links To File...\n')
        with open(os.getcwd()+'/file.txt', 'w') as f:
            for item in downloadLinks:
                f.write("%s\n" % item)
        sys.stdout.write('\r'+'File Ready.\n')

if __name__ == '__main__':
    sys.stdout.write('\r'+'Scanning for Links...\n')
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(sys.argv[1])

    scraper = Scraper(driver.find_element_by_xpath(
        "//table[@class='c']")).getDownloadLinks()
