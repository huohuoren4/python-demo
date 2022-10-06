import pytest
import requests
from utils.yaml_util import YamlUtil

token = ""
iam = YamlUtil("./testcases/yaml/iam.yaml").read()

@pytest.fixture(scope="session")
def get_token():
    """获取 token """
    global token
    if len(token) == 0:
        url = iam["IAM"]["获取token-url"]
        data = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "domain": {
                                "name": iam["IAM"]["IAMDomain"]
                            },
                            "name": iam["IAM"]["IAMUser"],
                            "password": iam["IAM"]["IAMPassword"]
                        }
                    }
                },
                "scope": {
                    "project": {
                        "name": iam["IAM"]["project_name"]
                    }
                }
            }
        }
        headers= {
            "Content-Type": "application/json"
        }
        res = requests.Request(method="POST", url=url, data=data, headers=headers)
    return token
