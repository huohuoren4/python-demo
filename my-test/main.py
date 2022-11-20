import logging
import time
from selenium import webdriver

from core.webui.element import Element

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    el = Element(driver=driver, log=logging.getLogger(), sleep_debug=0)
    el.get_url("https://v3.bootcss.com/getting-started/#download")
    el.slide_scrollbar(x=0, y=600)
    el.click_ele(value="/html/body/div[2]/div/div[1]/div[1]/div[3]/button")
    el.find_ele_visible(value='//*[text()="Copied!"]')
    print("\033[32mSuccess:字符串 (^_^)\033[0m")
    paste_content = el.get_paste()
    print(paste_content)
    el.click_ele(value="/html/body/div[2]/div/div[1]/div[1]/div[4]/button")
    print("\033[32mSuccess:字符串 (^_^)\033[0m")
    paste_content = el.get_paste()
    print(paste_content)
    el.click_ele(value="/html/body/div[2]/div/div[1]/div[1]/div[2]/button")
    print("\033[32mSuccess:字符串 (^_^)\033[0m")
    paste_content = el.get_paste()
    print(paste_content)
    time.sleep(300)
    driver.quit()
