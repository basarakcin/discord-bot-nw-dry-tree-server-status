from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
driver.get(URL)

def getServerStatus(server_name):
        driver.get(URL)
        data = []
        table = driver.find_element(By.TAG_NAME, 'tbody') 
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
                txt = row.text
                if server_name in txt:
                        raw_data = txt.split("\n")
                        data.append(raw_data[0])
                        data.append(raw_data[2].split(" ", 5)[4])
                        print(data) # DEBUG
        data.append("Status: " + data[0] + " " + status_emoji[data[0]])   
        data.append(data[1] +  " / 2,000")             
        return data[2:]
