import pytest
from requests import request

from utils.log_util import log
from utils.yaml_util import YamlUtil, yaml_variables_substitute

session_data = {"token": ""}
common_data = YamlUtil("testcases/yaml/common.yaml").read()
iam_data = yaml_variables_substitute(YamlUtil("testcases/yaml/iam.yaml").read(), common_data)


@pytest.fixture()
def get_token():
    """获取 token """
    global session_data
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
    log.info("获取了token")
    return session_data
