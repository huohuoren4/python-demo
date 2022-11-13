import os
import sys
import time
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://v3.bootcss.com/")
    driver.implicitly_wait(1)
    os.rename()

