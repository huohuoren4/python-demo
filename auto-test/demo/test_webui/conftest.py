import pytest
from demo.test_webui import webui_log, webui_session, s_driver
from demo.test_webui.page.login_page import LoginPage
from utils.file_util import YamlUtil

common_testcase_data = YamlUtil("demo/test_webui/config/testcase_config/common_testcase.yaml").read()
common_data = YamlUtil("demo/test_webui/config/common.yaml").read()
common_page_data = YamlUtil("demo/test_webui/config/page_config/common_page.yaml").read()
login_obj = LoginPage(driver=s_driver, log=webui_log, common_data=common_data, common_page_data=common_page_data)


@pytest.fixture(scope="session", autouse=True)
def run_webui():
    """运行 WebUI自动化框架 """
    webui_log.info("#################    WebUI 自动化开始运行!!!    #################")
    yield
    s_driver.quit()
    webui_log.info("#################    WebUI 自动化已经关闭!!!    #################")
    webui_log.info("")


@pytest.fixture(scope="module", autouse=True)
def login_global():
    """每个模块都会运行登录函数"""
    if not webui_session["is_login"]:
        login_obj.enter_login_page()
        login_obj.login_form(form_datas=common_testcase_data["登录页面"]["登录页面_用户名的校验01"]["表单数据"],
                             v_data=common_testcase_data["登录页面"]["登录页面_用户名的校验01"]["验证字段_断言数据"][0])
        assert login_obj.query_login_success(), "登录失败 !!!"
