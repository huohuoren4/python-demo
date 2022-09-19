import pytest
import yaml

def read_yml(filepath) :
    with open(filepath, encoding='utf8') as f :
        return yaml.load(f, Loader=yaml.FullLoader)

def write_yml(filepath, data) :
    with open(filepath, 'w') as f :
        yaml.dump(data, f)

@pytest.mark.parametrize('data1',read_yml("testcases/yaml/testcases.yml") )
def test_home(data1) :
    print(data1)


