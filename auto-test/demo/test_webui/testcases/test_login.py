import pytest

from demo.test_webui import s_element
from demo.test_webui.page.login_page import LoginPage
from utils.file_util import YamlUtil

login_obj = LoginPage()
login_obj.element = s_element
common_testcase_data = YamlUtil("demo/test_webui/config/testcase_config/common_testcase.yaml").read()


@pytest.fixture(autouse=True)
def login_page():
    login_obj.logout()


class TestLogin:
    @pytest.mark.parametrize("v_data", common_testcase_data["登录页面"]["登录页面_用户名的校验01"]["验证字段_断言数据"])
    def test_login_username_valid01(self, v_data):
        """登录页面_用户名的校验01: 正向"""
        login_obj.login_form(form_datas=common_testcase_data["登录页面"]["登录页面_用户名的校验01"]["表单数据"], v_data=v_data)
        assert login_obj.query_login_success(), "登录页面用户名的校验失败, 验证用户名: " + v_data[0]["v_char"]

    @pytest.mark.parametrize("v_data", common_testcase_data["登录页面"]["登录页面_用户名的校验02"]["验证字段_断言数据"])
    def test_login_username_valid02(self, v_data):
        """登录页面_用户名的校验01: 逆向"""
        login_obj.login_form(form_datas=common_testcase_data["登录页面"]["登录页面_用户名的校验02"]["表单数据"], v_data=v_data)
        assert login_obj.query_error_tip(v_data[1]["assert_text"]), "登录页面用户名的校验失败, 验证用户名: " + v_data[0]["v_char"]
