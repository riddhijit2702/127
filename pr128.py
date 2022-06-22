from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("./chromedriver")
browser.get(START_URL)
time.sleep(10)
# headers = ["Star","Constellation","Right Ascension","Declination","Distance","Mass"]
planet_data = []
new_planet_data = []


soup = BeautifulSoup(browser.page_source, "html.parser")

for tr_tag in soup.find_all("tr"):
           
    temp_list = []
for  td_tag in tr_tag:
    td_tags = td_tag.find_all("td")
    temp_list.append(td_tag.contents[0])
planet_data.append(temp_list)

Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)       


