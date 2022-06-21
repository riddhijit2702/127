from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("./chromedriver")
browser.get(START_URL)
time.sleep(10)
headers = ["Star","Constellation","Right Ascension","Declination","Distance","Mass"]
planet_data = []
new_planet_data = []
def scrape():
 
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for tr_tag in soup.find_all("tr"):
           
            temp_list = []
            for  td_tag in td_tags:
                td_tags = tr_tag.find_all("td")
                temp_list.append(td_tag.contents[0])
            planet_data.append(temp_list)

        for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
        planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()    

scrape()
final_planet_data = []
