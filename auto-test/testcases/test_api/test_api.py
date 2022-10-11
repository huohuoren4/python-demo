import pytest
from requests import request
from conftest import common_data
from utils.log_util import log
from utils.yaml_util import YamlUtil, yaml_variables_substitute, string_variables_substitute

ief_data = yaml_variables_substitute(YamlUtil("testcases/test_api/yaml/ief.yaml").read(), common_data)


class TestApi:
    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表"]["验证字段"]["v_token"])
    def test_app_template_getlist(self, get_token, v_datas):
        '''查询应用模板列表: X-Auth-Token 正向'''
        # 获取数据
        session_data = get_token
        v_datas = string_variables_substitute(v_datas, session_data)
        app_template_data = yaml_variables_substitute(ief_data["边缘应用"]["应用模板"]["查询应用模板列表"], session_data)
        app_template_data = yaml_variables_substitute(app_template_data, {"v_token": v_datas})
        url = app_template_data["url"]
        method = app_template_data["method"]
        data = app_template_data["data"]
        json = app_template_data["json"]
        headers = app_template_data["headers"]
        params = app_template_data["params"]
        files = app_template_data["files"]
        timeout = float(app_template_data["timeout"])
        log.info("%s : %s 验证数据: %s", method, url, v_datas)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        assert res.status_code < 300

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表01"]["验证字段"]["v_token"])
    def test_app_template_getlist01(self, get_token, v_datas):
        '''查询应用模板列表: X-Auth-Token 逆向'''
        # 获取数据
        session_data = get_token
        v_datas = string_variables_substitute(v_datas, session_data)
        app_template_data = yaml_variables_substitute(ief_data["边缘应用"]["应用模板"]["查询应用模板列表01"], session_data)
        app_template_data = yaml_variables_substitute(app_template_data, {"v_token": v_datas})
        url = app_template_data["url"]
        method = app_template_data["method"]
        data = app_template_data["data"]
        json = app_template_data["json"]
        headers = app_template_data["headers"]
        params = app_template_data["params"]
        files = app_template_data["files"]
        timeout = float(app_template_data["timeout"])
        log.info("%s : %s 验证数据: %s", method, url, v_datas)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        assert res.status_code >= 300

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表02"]["验证字段"]["v_instance_id"])
    def test_app_template_getlist02(self, get_token, v_datas):
        '''查询应用模板列表: ief-instance-id 正向'''
        # 获取数据
        session_data = get_token
        v_datas = string_variables_substitute(v_datas, session_data)
        app_template_data = yaml_variables_substitute(ief_data["边缘应用"]["应用模板"]["查询应用模板列表02"], session_data)
        app_template_data = yaml_variables_substitute(app_template_data, {"v_instance_id": v_datas})
        url = app_template_data["url"]
        method = app_template_data["method"]
        data = app_template_data["data"]
        json = app_template_data["json"]
        headers = app_template_data["headers"]
        params = app_template_data["params"]
        files = app_template_data["files"]
        timeout = float(app_template_data["timeout"])
        log.info("%s : %s 验证数据: %s", method, url, v_datas)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        assert res.status_code < 300

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表03"]["验证字段"]["v_instance_id"])
    def test_app_template_getlist03(self, get_token, v_datas):
        '''查询应用模板列表: ief-instance-id 逆向'''
        # 获取数据
        session_data = get_token
        v_datas = string_variables_substitute(v_datas, session_data)
        app_template_data = yaml_variables_substitute(ief_data["边缘应用"]["应用模板"]["查询应用模板列表03"], session_data)
        app_template_data = yaml_variables_substitute(app_template_data, {"v_instance_id": v_datas})
        url = app_template_data["url"]
        method = app_template_data["method"]
        data = app_template_data["data"]
        json = app_template_data["json"]
        headers = app_template_data["headers"]
        params = app_template_data["params"]
        files = app_template_data["files"]
        timeout = float(app_template_data["timeout"])
        log.info("%s : %s 验证数据: %s", method, url, v_datas)
        res = request(method=method, url=url, params=params, data=data, json=json, files=files, headers=headers,
                      timeout=timeout)
        assert res.status_code >= 300
