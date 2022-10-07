import logging

from requests import request

from confest import get_token, common_data
from utils import log_util
from utils.log_util import log
from utils.yaml_util import YamlUtil, yaml_variables_substitute

ief_data = yaml_variables_substitute(YamlUtil("testcases/yaml/ief.yaml").read(), common_data)


class TestApi:
    def test_app_template_getlist(self, get_token):
        '''查询应用模板列表'''
        # 获取数据
        session_data = get_token
        session_data["node_id"] = "111111111111111111111111111"
        app_template_data = yaml_variables_substitute(ief_data["边缘应用"]["应用模板"]["查询应用模板列表"], session_data)
        url = app_template_data["url"]
        method = app_template_data["method"]
        data = app_template_data["data"]
        json = app_template_data["json"]
        headers = app_template_data["headers"]
        params = app_template_data["params"]
        files = app_template_data["files"]
        timeout = float(app_template_data["timeout"])
        log.info("%s : %s", method, url)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        assert res.status_code < 300

    def test_app_template_get01(self, get_token):
        '''查询应用模板列表'''
        # 获取数据
        session_data = get_token
        print(session_data)
        app_template_data = yaml_variables_substitute(ief_data["边缘应用"]["应用模板"]["查询应用模板列表"], session_data)
        url = app_template_data["url"]
        method = app_template_data["method"]
        data = app_template_data["data"]
        json = app_template_data["json"]
        headers = app_template_data["headers"]
        params = app_template_data["params"]
        files = app_template_data["files"]
        timeout = float(app_template_data["timeout"])
        log.info("%s : %s", method, url)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        assert res.status_code < 300
