# !/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time

def click():
    while True :
        browser.find_element_by_link_text("点我").click()
        time.sleep(1)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
browser.get("https://detail.tmall.com/item.htm?spm=a1z10.4-b-s.w5003-22082778529.6.3f001e00vAe7Tn&id=603123506400")
click()