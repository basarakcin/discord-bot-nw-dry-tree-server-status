from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
driver.get(URL)

def getServerStatus(server_name):
        data={}
        driver.get(URL)
        table = driver.find_element(By.TAG_NAME, 'tbody') 
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
                txt = row.text
                if server_name in txt:
                        raw_data = txt.split("\n")
                        data['availability'] = raw_data[0]
                        data['online-players'] = raw_data[2].split(" ", 5)[4] # This line MUST be edited for other servers
        return data
