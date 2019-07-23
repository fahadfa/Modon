#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 01:20:44 2019

@author: manzar
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.modon.gov.sa/ar/IndustrialCities/Pages/factories.aspx"

prefs = {
  "translate_whitelists": {"fr":"en"},
  "translate":{"enabled":"true"}
}

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)

wb = webdriver.Chrome(chrome_options=options)
wb.get(url)

link = 'https://www.modon.gov.sa/ar/IndustrialCities/Pages/factory.aspx?factoryId='
header = "Company name, Telephone, Fax, Email\n"
file = open("assignment.csv", "a")
file.write(header)
for i in range(3994, 7812):
    wb.get(link + str(i))
    time.sleep(1)
    html = wb.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(html, 'lxml')
    try:
        table = soup.findAll('table', {'class': 'ModonInfoTable'})
        td = table[0].findAll('td')
        td = td[1::2]
        try:
            name = td[0].text
        except:
            name = 'NaN'
            
        try:
            tel = td[2].text
        except:
            tel = 'NaN'
            
        try:
            fax = td[3].text
        except:
            fax = 'NaN'
            
        try:
            email = td[-2].text
        except:
            email = 'NaN'
        
        print(name, tel, fax, email)
        file.write(name.replace(',', '').lstrip() + ', ' + tel + ', ' + fax + ', ' + email + '\n')
    except:
        print('NaN')
            
file.close()
        
        
        