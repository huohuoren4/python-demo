import os

import pytest

ROOT_DIR = os.path.dirname(__file__)

# 跑 API 自动化设置 UI_SWITCH = False
# 开关 UI 自动化测试
UI_SWITCH = False

"""
Web-UI 自动化测试
"""

if __name__ == '__main__':
    pytest.main()
    # cmd = r"allure generate ./allure_reports/tmp  -o ./allure_reports/html --clean"
    # os.system(cmd)
