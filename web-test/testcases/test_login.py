from time import sleep

from page.element import find_ele


class TestLogin:
    def test_tooltip(self, get_driver):
        find_ele(get_driver, value="/html/body/div[2]/div/div[1]/div[7]/div[3]/div/button[1]").click()
        find_ele(get_driver, value="//div[@class='tooltip fade left in']")
        sleep(60)


