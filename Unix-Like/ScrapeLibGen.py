import os, sys, re, time
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:
    def __init__(self, webtable):
        self.table = webtable
        self.links = []
        self.downloadLinks = []
        self.authors = []
        self.titles = []

    def getLinks(self):
        sys.stdout.write("\r" + "Fetching Download Links.\n")
        for link in self.getDownloadLinks():
            driver.get(link)
            dl = driver.find_element(By.XPATH, '//*[@id="download"]/ul/li[1]/a')
            self.downloadLinks.append(dl.get_attribute("href"))

        self.getList(list_type="titles", col_no=3)
        # self.getList(list_type="authors", col_no=2)
        # self.writeToFile(self.downloadLinks)

    def getDownloadLinks(self, column_number=10):
        sys.stdout.write("\r" + "Preparing Links For Download...\n")
        linksColumn = self.table.find_elements(
            By.XPATH, "//tr/td[" + str(column_number) + "]/a"
        )
        for webElement in linksColumn:
            self.links.append(webElement.get_attribute("href"))
        sys.stdout.write("\r" + "Links Prepared.\n")
        return self.links

    def writeToFile(self, downloadLinks):
        sys.stdout.write("\r" + "Writing Download Links To File...\n")
        with open(os.getcwd() + "/download_links.txt", "w") as f:
            for line in downloadLinks:
                f.write("%s\n" % line)
                os.system("wget -c " + line)
        sys.stdout.write("\r" + "File Ready. \n")

    def getList(self, list_type, col_no):
        sys.stdout.write("\r" + "Preparing List of " + list_type + " for Download...\n")
        column = self.table.find_elements(By.XPATH, "//tr/td[" + str(col_no) + "]")
        sys.stdout.write("\r" + "Fetching " + list_type + "\n")
        if list_type == "titles":
            for webElement in column:
                txt = (webElement.text).replace("\n", " ")
                txt = txt.replace(", ", "")
                # replace trailing digits from end of string:
                txt = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", txt)
                self.titles.append(txt)
            sys.stdout.write(list_type + " list prepared.\n")
            del self.titles[:2]
            del self.titles[-1]
            sys.stdout.write(
                "\n".join(str(str(i + 1) + "\t" + x) for i, x in enumerate(self.titles))
            )
            return self.titles
        elif list_type == "authors":
            for webElement in column:
                txt = (webElement.text).replace("\n", " ")
                txt = txt.replace(", ", " ")
                txt = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", txt)
                self.authors.append(txt)
            sys.stdout.write(list_type + " list prepared.\n")
            del self.authors[:3]
            del self.authors[-1]
            sys.stdout.write(
                "\n".join(
                    str(str(i + 1) + "\t" + x) for i, x in enumerate(self.authors)
                )
            )
            return self.authors


if __name__ == "__main__":
    options = Options()
    options.binary_location = "/bin/brave"
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    sys.stdout.write("\r" + "Scanning for Links...\n")
    driver.get(sys.argv[1])

    Scraper(driver.find_element(By.XPATH, "//table[@class='c']")).getLinks()
