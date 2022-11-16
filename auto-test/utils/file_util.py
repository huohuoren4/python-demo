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

    .. 使用方法::
        yaml_data= YamlUtil("testcases/yaml/testcases.yml").read()
        @pytest.mark.parametrize('data', yaml_data)
        def test_home(data):
            print(data)
    """

    def __init__(self, filename: str) -> None:
        """
        初始化方法

        :param filename: yaml文件名
        """
        self.filename = deal_path(filename)

    def read(self) -> dict:
        """
        读yaml文件

        :return: 返回一个字典类型数据
        """
        with open(self.filename, encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def write(self, data: dict) -> None:
        """
        写入yaml文件

        :param data: 字典类型数据
        :return:
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)


def deal_path(path: str) -> str:
    """
    路径处理

    所有文件路径都是从根目录开始写, 可以参考示例

    :param path: 文件路径
    :return: 返回一个路径字符串

    .. 使用示例::
        # 从根目录开始写
        path= "testcases/test-api.py"
        deal_path(path)
    """
    return os.path.join(ROOT_DIR, path.replace("/", os.path.sep))


def yaml_variables_substitute(template: Any, data: dict) -> Any:
    """
    解析 yaml 文件中的变量

    变量的正则表达式: `r'[_a-z][_a-z0-9]*'`, 换句话说就是 `python` 变量的命名规则
    
    :param template: 模板, 可以是字符串也可以是字典
    :param data:  带变量名与变量值的数据, 可以是字符串也可以是字典
    :return: 可以是字符串也可以是字典, 和`template`的数据类型保持一致

    .. 使用示例::
        yaml_variables_substitute({ "name": "this is ${name}"}, { "name" : "123"})
        # 输出: { "name": "this is 123"}
    """
    template = json.dumps(template)
    if re.search(r"\${.+?}", template):
        template = Template(template).safe_substitute(data)
    return json.loads(template)
