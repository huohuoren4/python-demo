import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://v5.bootcss.com/")
    driver.implicitly_wait(5)
    driver.execute_script()
    start_time = time.time()
    locator = ("xpath", '//*[@id="content"]/div/div/div[2]/div/a[1]')
    try:
        WebDriverWait(driver, timeout=3).until(expected_conditions.presence_of_element_located(locator))
    except TimeoutException as e:
        print(e)
    total_time = time.time() - start_time
    print("\033[32mSuccess:字符串 (^_^)\033[0m", total_time)
    time.sleep(3)
    driver.implicitly_wait(0)
    start_time = time.time()
    locator = ("xpath", '//*[@id="content"]/div/div[2]/a')
    try:
        WebDriverWait(driver, timeout=3).until_not(expected_conditions.presence_of_element_located(locator))
    except TimeoutException as e:
        print(e)
    total_time = time.time() - start_time
    print("\033[32mSuccess:字符串 (^_^)\033[0m", total_time)
    time.sleep(3)

    driver.quit()
