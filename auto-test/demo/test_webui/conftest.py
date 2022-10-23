import pytest
from demo.test_webui import webui_log, s_element, webui_session
from demo.test_webui.page.login_page import LoginPage
from utils.file_util import YamlUtil

common_testcase_data = YamlUtil("demo/test_webui/config/testcase_config/common_testcase.yaml").read()
login_obj = LoginPage()
login_obj.element = s_element


@pytest.fixture(scope="session", autouse=True)
def run_webui():
    """运行 WebUI自动化框架 """
    webui_log.info("#################    WebUI 自动化开始运行!!!    #################")
    yield
    s_element.driver.quit()
    webui_log.info("#################    WebUI 自动化已经关闭!!!    #################")
    webui_log.info("")


@pytest.fixture(scope="module", autouse=True)
def login_global():
    """每个模块都会运行登录函数"""
    if not webui_session["is_login"]:
        login_obj.enter_login_page()
        login_obj.login_form(form_datas=common_testcase_data["登录页面"]["登录页面_用户名的校验01"]["表单数据"],
                             v_data=common_testcase_data["登录页面"]["登录页面_用户名的校验01"]["验证字段_断言数据"][0])
        login_obj.query_login_success()
