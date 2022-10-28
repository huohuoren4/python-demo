import re
from logging import Logger
from typing import List

from requests import request, Response
from utils.file_util import yaml_variables_substitute


def request_template(req_data: dict, log: Logger, session_data: dict, v_datas: List[dict]) -> Response:
    """
    API 接口请求模板
    @param v_datas: 验证数据和断言数据
    @param log: 日志对象
    @param session_data: 动态数据
    @param req_data: 模板数据
    @return:
    """
    v_datas = yaml_variables_substitute(v_datas, session_data)
    if v_datas[0]:
        for key, value in v_datas[0].items():
            session_data[key] = value
        req_data = yaml_variables_substitute(req_data, session_data)
    log.info("%s : %s\t验证数据:%s,断言数据:%s", req_data["method"], req_data["url"], str(v_datas[0]), str(v_datas[1]))
    res = request(method=req_data["method"], url=req_data["url"], params=req_data["params"], data=req_data["data"],
                  json=req_data["json"], files=req_data["files"], headers=req_data["headers"],
                  timeout=float(req_data["timeout"]))
    assert res.status_code == int(v_datas[1]["status_code"]), "HTTP 响应失败, 实际的状态码: " + str(res.status_code)
    if v_datas[1]["assert_text"]:
        for value in v_datas[1]["assert_text"]:
            assert re.search(value, res.text), "响应数据断言错误, 响应文本: " + res.text
    return res
