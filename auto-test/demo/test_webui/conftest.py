import pytest
from demo.test_webui import webui_log, s_element
from demo.test_webui.page_element import login_obj


@pytest.fixture(scope="session", autouse=True)
def run_webui():
    """运行 WebUI自动化框架 """
    webui_log.info("#################    WebUI 自动化开始运行!!!    #################")
    # 登录
    # login_obj.login()
    yield
    s_element.driver.quit()
    webui_log.info("#################    WebUI 自动化已经关闭!!!    #################")
    webui_log.info("")