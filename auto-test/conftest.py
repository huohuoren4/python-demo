import pytest

from core.api_core import api_template
from main import UI_SWITCH
from core.element import single_ele
from requests import request
from utils.log_util import single_log
from utils.file_util import YamlUtil, yaml_variables_substitute


# 获取驱动
@pytest.fixture(scope="session", autouse=UI_SWITCH)
def get_driver():
    """获取 driver """
    single_ele.driver.set_page_load_timeout(10)
    single_ele.driver.implicitly_wait(5)
    single_ele.driver.maximize_window()
    yield
    single_ele.driver.quit()


session_data = {"token": ""}
common_data = YamlUtil("testcases/test_api/yaml//common.yaml").read()
iam_data = yaml_variables_substitute(YamlUtil("testcases/test_api/yaml//iam.yaml").read(), common_data)


@pytest.fixture()
def get_token():
    """获取 token, 未考虑 token 的过期时间"""
    if len(session_data["token"]) == 0:
        res = api_template(req_data=iam_data["获取token"], session_data=session_data,
                           v_datas=iam_data["获取token"]["验证字段_断言数据"][0])
        session_data["token"] = res.headers["X-Subject-Token"]
        single_log.info("获取了token")
    return session_data
