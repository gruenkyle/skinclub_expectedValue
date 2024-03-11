#######################################
#
#      Method To Create Dictionary 
#   Given a URL to Case Information 
# Returns Dictionary of Information to Process
#
#          Author : Kyle Gruen
#          Date : 02/27/2024
#
#######################################

# Import Statements #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

from webdriver_manager.chrome import ChromeDriverManager

# Main Method #

def createDictionary(url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)
    wait = WebDriverWait(driver, 10)

    get_url = driver.current_url

    wait.until(EC.url_to_be(url))
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'table-cell')))

    if get_url == url:

        page_source = driver.page_source


    soup = BeautifulSoup(page_source, features='html.parser')

    oddDiv = soup.find_all('div', class_='table-cell odds')
    priceDiv = soup.find_all('span', class_='price')

    

    mainFrame = pd.DataFrame(columns=['Odd'])
    priceFrame = pd.DataFrame(columns=['Price'])

    for odd in oddDiv:
        mainFrame = mainFrame._append({'Odd': odd.text.strip()}, ignore_index=True)
    for price in priceDiv:
        if "-" in price:
            price = price.split("-")[0]
        priceFrame = priceFrame._append({'Price': price.text.strip()}, ignore_index=True)

    driver.quit()

    odds = mainFrame.iloc[1::2].reset_index(drop=True)
    prices = priceFrame.iloc[1:].reset_index(drop=True)

    odds['Odd'] = odds['Odd'].str.replace("%", '').astype(float)
    prices['Price'] = prices['Price'].str.replace("$", '').astype(float)

    odds['Odd'] = odds['Odd'] * 0.01

    caseName = url.split('/')[-1]

    expectation = (odds['Odd'] * prices['Price']).sum()

    caseDictionary = {
        'CaseName': caseName,
        'Odds': odds,
        'Prices': prices,
        'Expectation': expectation
    }

    return caseDictionary
