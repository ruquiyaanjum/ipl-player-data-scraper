from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
import os
os.chdir("c:/Users/ruqui/Downloads")

options=webdriver.ChromeOptions()
options.headleass=True

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.iplt20.com/teams/royal-challengers-bengaluru/squad-details/164")
driver.implicitly_wait(10)

html_doc=driver.page_source
soup=BeautifulSoup(html_doc,"html.parser")

table=soup.find("table",class_="sm-pp-table")
table_column=table.find("thead").find_all("th")
table_column1=[]
for i in table_column:
    table_column1.append(i.text.strip())
table_row=[]
table_rows=table.find("tbody").find_all("tr")
for i in table_rows:
    columns=i.find_all("td")
    if len(columns) > 0:
        b={}
        for j,column in enumerate(columns):
            b[table_column1[j]]=column.text.strip()
        table_row.append(b)

with open("ipl_data.csv","w") as f:
    writer=csv.DictWriter(f,fieldnames=table_column1)
    writer.writeheader()
    writer.writerows(table_row)
print("data store in csv file")
driver.quit()