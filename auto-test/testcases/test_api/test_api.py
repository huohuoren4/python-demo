import pytest
from conftest import common_data
from core.api_core import api_template
from utils.file_util import YamlUtil, yaml_variables_substitute

ief_data = yaml_variables_substitute(YamlUtil("testcases/test_api/yaml/ief.yaml").read(), common_data)


class TestApi:
    """
    查询应用模板列表0: X-Auth-Token 正向
    """

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表"]["验证字段_断言数据"])
    def test_app_template_getlist(self, get_token, v_datas):
        """查询应用模板列表: X-Auth-Token 正向"""
        api_template(req_data=ief_data["边缘应用"]["应用模板"]["查询应用模板列表"], session_data=get_token, v_datas=v_datas)

    """
    查询应用模板列表01: X-Auth-Token 逆向
    """

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表01"]["验证字段_断言数据"])
    def test_app_template_getlist01(self, get_token, v_datas):
        """查询应用模板列表01: X-Auth-Token 逆向"""
        api_template(req_data=ief_data["边缘应用"]["应用模板"]["查询应用模板列表01"], session_data=get_token, v_datas=v_datas)

    """
    查询应用模板列表02: ief-instance-id 正向"
    """

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表02"]["验证字段_断言数据"])
    def test_app_template_getlist02(self, get_token, v_datas):
        """查询应用模板列表02: ief-instance-id 正向"""
        api_template(req_data=ief_data["边缘应用"]["应用模板"]["查询应用模板列表02"], session_data=get_token, v_datas=v_datas)

    """
    查询应用模板列表03: ief-instance-id 逆向
    """

    @pytest.mark.parametrize("v_datas", ief_data["边缘应用"]["应用模板"]["查询应用模板列表03"]["验证字段_断言数据"])
    def test_app_template_getlist03(self, get_token, v_datas):
        """查询应用模板列表03: ief-instance-id 逆向"""
        api_template(req_data=ief_data["边缘应用"]["应用模板"]["查询应用模板列表03"], session_data=get_token, v_datas=v_datas)
