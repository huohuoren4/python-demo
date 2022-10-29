import time
import pytest
from core.api.api_core import request_template
from demo.test_api.initial import api_log, session_data, common_data
from utils.file_util import yaml_variables_substitute, YamlUtil

iam_data = yaml_variables_substitute(YamlUtil("demo/test_api/config/iam.yaml").read(),
                                     common_data)


@pytest.fixture(scope="session", autouse=True)
def run_api():
    """运行接口自动化框架 """
    time.sleep(1)
    api_log.info("#################      接口自动化开始运行!!!     #################")
    yield
    api_log.info("#################      接口自动化已经关闭!!!     #################")
    api_log.info("")


@pytest.fixture()
def get_token() -> dict:
    """获取华为云IAM的token, 考虑 token 的过期时间"""
    if time.time() > session_data["expire_time"]:
        res = request_template(req_data=iam_data["获取token"], log=api_log, session_data=session_data,
                               v_datas=iam_data["获取token"]["验证字段_断言数据"][0])
        session_data["token"] = res.headers["X-Subject-Token"]
        # 设置过期时间 1s, 这是一个测试时间; 实际上, token的过期时间需要从响应数据中获取
        session_data["expire_time"] = time.time() + 1
        api_log.info("获取了token")
    return session_data
