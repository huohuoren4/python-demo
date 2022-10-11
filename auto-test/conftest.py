import pytest

from main import UI_SWITCH
from page.element import ele
from requests import request
from utils.log_util import log
from utils.yaml_util import YamlUtil, yaml_variables_substitute


# 获取驱动
@pytest.fixture(scope="session", autouse=UI_SWITCH)
def get_driver():
    """获取 driver """
    ele.driver.set_page_load_timeout(10)
    ele.driver.implicitly_wait(5)
    ele.driver.maximize_window()
    yield
    ele.driver.quit()


session_data = {"token": ""}
common_data = YamlUtil("testcases/test_api/yaml//common.yaml").read()
iam_data = yaml_variables_substitute(YamlUtil("testcases/test_api/yaml//iam.yaml").read(), common_data)


@pytest.fixture()
def get_token():
    """获取 token, 未考虑 token 的过期时间"""
    if len(session_data["token"]) == 0:
        iam_api_data = iam_data["获取token"]
        url = iam_api_data["url"]
        method = iam_api_data["method"]
        data = iam_api_data["data"]
        json = iam_api_data["json"]
        headers = iam_api_data["headers"]
        params = iam_api_data["params"]
        files = iam_api_data["files"]
        timeout = float(iam_api_data["timeout"])
        log.info("%s: %s", method, url)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        if res.status_code < 300:
            session_data["token"] = res.headers["X-Subject-Token"]
        log.info("更新了token")
    return session_data
