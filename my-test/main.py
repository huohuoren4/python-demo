import logging
from time import sleep

from selenium import webdriver

from core.webui.element import Element

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://v3.bootcss.com/")
    driver.implicitly_wait(1)
    ele = Element(driver= driver, log=logging.getLogger(), sleep_debug=0)
    driver.find_element("xpath", '//*[@id="content"]/div/p[2]/a').click()
    ele.slide_scrollbar(0, 500)
    driver.find_element("xpath", '/html/body/div[2]/div/div[1]/div[1]/div[3]/button').click()

    print(ele.get_paste())

    sleep(300)
    driver.quit()

