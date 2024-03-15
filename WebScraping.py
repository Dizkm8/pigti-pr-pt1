# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:51:34 2023

@author: bmo
"""

# import module
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver
# folder of the root directory.

driver = webdriver.Chrome()

driver.get("https://www.scrapethissite.com/pages/simple/")
  
# Maximize the window and let code stall 
# for 10s to properly maximize the window.
driver.maximize_window()
time.sleep(10)

# Ingresar datos de ingreso

NombrePaises = driver.find_elements(By.CLASS_NAME, "country-name")
ListaPaises = []
for i in NombrePaises:
    ListaPaises.append(i.text)

# print(ListaPaises)
time.sleep(5)

ListaCapitales = []
NombreCapitales = driver.find_elements(By.CLASS_NAME, "country-capital")
for x in NombreCapitales:
    ListaCapitales.append(x.text)

populationLists = []
populationsValues = driver.find_elements(By.CLASS_NAME, "country-population")
for x in populationsValues:
    populationLists.append(x.text)

print(ListaCapitales)

time.sleep(5)

driver.close()
