from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def waitfor(myxpath,sec,element):
        try:
            myobj=WebDriverWait(driver,sec).until(EC.presence_of_element_located((By.XPATH,myxpath)))
            return myobj
        except:
            print(element)


driver = webdriver.Chrome("C:\Python27\chromedriver") #enter your chrome driver path here
driver.get("https://www.nvsp.in/")


search = driver.get("http://electoralsearch.in/")

continue1 = driver.find_element_by_id("continue")
continue1.click()

name = "Pragati" #enter name to be searched in electrol roll
fname = "Pandurang" #father's name
tname = driver.find_element_by_id("name1")
tname.send_keys(name)
tname.send_keys(Keys.RETURN)


father_name = driver.find_element_by_id("txtFName")
father_name.send_keys(fname)
father_name.send_keys(Keys.RETURN)


age = Select(driver.find_element_by_id('ageList'))
age.select_by_value('4')

gender = Select(driver.find_element_by_id('listGender'))
gender.select_by_index('2')


state = Select(driver.find_element_by_id('nameStateList'))
state.select_by_index('20')

district = Select(driver.find_element_by_id('namelocationList'))
district.select_by_index('26')

PCaptch=waitfor('//*[@id="captchaDetailImg"]',10,'Captch Field')
PCaptch.clear()
captcha = send_keys(PCaptch)
captcha.send_keys(Keys.RETURN)
searchR = driver.find_element_by_id("btnDetailsSubmit")
searchR.click()

# PCaptch=waitfor('//*[@id="captchaDetailImg"]',10,'Captch Field')
