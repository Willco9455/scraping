from time import sleep

import os

from excel import ExcelHandle

from functions import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# sets perameters for selenium
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  
options.add_argument("--window-size=1920,1080")


# path of the chromedriver we have just downloaded
PATH = r"./chromedriver"

while True:
    # driver = webdriver.Chrome(PATH)  # to open the browser
    driver = webdriver.Chrome(PATH, chrome_options=options)
    excelHandle =  ExcelHandle()
    
    # Loads site and resizes window
    url = "https://www.epo.org/learning/eqe/successful-candidates.html"
    driver.get(url)
    driver.maximize_window()
    sleep(0.2)

    # accepts cookies
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="matomoBanner"]/div/div/table/tbody/tr/td[2]/button'))).click()



    while True:
        os.system('CLS')
        name = input('Name: ')
        name = name.capitalize()
        year = input('Year: ')
        nationality = input('Nationality: ')
        nationality = nationality.title()
        
        if name != '':
            try:
                driver.execute_script(f"document.getElementById('eqeQueryName').setAttribute('value', '{name}')")
            except:
                os.system('CLS')
                print('Invalid Name Entered')
                sleep(2)
                continue
        if year != '':
            try:
                select = Select(driver.find_element(By.ID, 'eqeQueryYear'))
                select.select_by_value(year)
            except:
                os.system('CLS')
                print('Invalid Year Entered')
                sleep(2)
                continue
        if nationality != '':
            try:
                select = Select(driver.find_element(By.ID, 'eqeQueryCountry'))
                select.select_by_visible_text(nationality)
            except:
                os.system('CLS')
                print('Invalid Country Entered')
                sleep(2)
                continue
        break
    os.system('CLS')


    def scrapePage(count, resAmount):
        sleep(0.5)
        # gets all items in list
        # element = WebDriverWait(driver, 20).until(EC.((By.CLASS_NAME, "listItem")))
        results = driver.find_elements(By.CLASS_NAME, "listItem")
        # print(results[0].text)
        # clicks on each item to load extra details
        for i in results:
            try:
                driver.execute_script("arguments[0].click()", i)
            except:
                pass

        # sleep(0.5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "vcard")))    
        # gets extra results from opened items in list
        if (len(results) < 10):
            sleep(1)
        # sleep(0.5)
        results = driver.find_elements(By.CLASS_NAME, "vcard")
        
        last = ''
        for i in range(0, len(results) - 1, 1):
            unformatted = results[i].text.split('\n')
            if last == (results[i].text) or unformatted[0] == '':
                continue
            last = results[i].text
            formatted = formatData(unformatted)
            excelHandle.addRow(formatted)
            count += 1
            
            # os.system('CLS')
            print(f'{count} of {resAmount}')

        return count, resAmount 


    # clicks search button to load results
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#eqeSearchSubmit"))).click()
    sleep(1)

    # selects the page results to display 50 results
    amountButton = driver.find_element(By.XPATH, '//*[@id="epoEqeResults"]/div[2]/div/ul/li[3]')
    driver.execute_script("arguments[0].click()", amountButton)

    # gets the number of results returned as a number
    results = driver.find_element(By.XPATH, '//*[@id="eqeResultList"]/span').text

    try:
        results = int(results.split(' ')[4])
    except:
        os.system('CLS')
        print('NO RESULTS FOUND')
        excelHandle.close()
        driver.close()
        input('Press Enter to Search Again')
        continue
    count = 0
    while True:
        if count >= results:
            print('SCRAPE COMPLETE')
            # input('Press Enter to search again')
            break
        driver.execute_script(f"window.scrollTo(0, {500})")
        count, results = scrapePage(count, results)
        
        # os.system('CLS')
        # print(f'{count} of {results}')
        sleep(0.6)
        try: 
            nextButton = driver.find_element(By.CLASS_NAME, 'next-link')
            nextButton = nextButton.find_element(By.LINK_TEXT, 'next')
            driver.execute_script("arguments[0].click()", nextButton)
        except: 
            print('SCRAPE COMPLETE')
            # input('Press Enter to search again')
            break
    excelHandle.close()
    driver.close()
    input('Press Enter to search again')
