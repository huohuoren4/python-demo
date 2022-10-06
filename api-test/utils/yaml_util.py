from typing import Any

import yaml


class YamlUtil:
    """
    yaml 文件配置类
    使用方法:
    @pytest.mark.parametrize('data1', Yaml("testcases/yaml/testcases.yml").read_yaml)
    def test_home(data1):
        print(data1)
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read(self) -> dict:
        with open(self.filename, encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def write(self, data: dict = {}) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)

