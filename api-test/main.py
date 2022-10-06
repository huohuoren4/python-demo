import os

import pytest

ROOT_DIR = os.path.dirname(__file__)

if __name__ == '__main__':
    pytest.main()
    # cmd = r"allure generate ./allure_reports/tmp  -o ./allure_reports/html --clean"
    # os.system(cmd)
