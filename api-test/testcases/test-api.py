import pytest
import requests
from utils.yaml_util import YamlUtil

ief_obj = YamlUtil("./yaml/ief.yaml")
ief_data = ief_obj.read()


class TestApi:
    @pytest.mark.parametrize("app_template_data", ief_data["IEF"]["边缘应用"]["应用模板"]["查询应用模板列表"])
    def test_app_template_getlist(get_token, app_template_data):
        '''函数说明'''
        url = app_template_data["url"]
        headers= {
            "Content-Type": "application/json"
        }
        res = requests.Request(method="POST", url=url, data=data, headers=headers)
