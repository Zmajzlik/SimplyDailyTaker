from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
waitTime1 = 60
waitTime2 = 86400
def GetFreeCase():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--user-data-dir=C:/Users/Zmajzlik/AppData/Local/Google/Chrome/User Data/Default")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://hellcase.com/en/dailyfree")
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "btn_open_daily_free")))   
    finally:
        driver.find_element_by_id("btn_open_daily_free").click();
        time.sleep(waitTime1)
        driver.quit()
while True:
    GetFreeCase()
    time.sleep(waitTime2)

