from time import sleep

from demo.test_webui.page_element import login_obj


class TestLogin:
    def test_login(self):
        login_obj.login()
        sleep(1)
