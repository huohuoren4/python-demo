import json
import os.path
import re
from string import Template
from typing import Any

import yaml
from main import ROOT_DIR


class YamlUtil:
    """
    yaml 文件配置类
    使用方法:
    @pytest.mark.parametrize('data1', Yaml("testcases/yaml/testcases.yml").read_yaml)
    def test_home(data1):
        print(data1)
    """

    def __init__(self, filename: str) -> None:
        self.filename = deal_path(filename)

    def read(self) -> dict:
        with open(self.filename, encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def write(self, data: dict) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)


def deal_path(path: str):
    """
    路径处理
    使用示例:
    path: 从根目录开始写 -- testcases/test-api.py
    deal_path(path)
    """
    return os.path.join(ROOT_DIR, path.replace("/", os.path.sep))


def yaml_variables_substitute(template: Any, data: dict) -> Any:
    """
    解析 yaml 文件中的变量
    变量的正则表达式: r'[_a-z][_a-z0-9]*', 换句话说就是 python 变量的命名规则
    使用示例:
    yaml_variables_substitute({ "name": "this is ${name}"}, { "name" : "123"}) # 输出: { "name": "this is 123"}
    """
    parse_str = json.dumps(template)
    template = string_variables_substitute(parse_str, data)
    return json.loads(template)


def string_variables_substitute(template: str, data: dict) -> str:
    """
    解析 yaml 文件中的变量
    变量的正则表达式: r'[_a-z][_a-z0-9]*', 换句话说就是 python 变量的命名规则
    使用示例:
    string_variables_substitute("this is ${name}", { "name" : "123"}) # 输出: "this is 123"
    """
    if re.search(r"\${.+?}", template):
        template = Template(template).safe_substitute(data)
    return template
