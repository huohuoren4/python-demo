import os
import pytest

"""
Autotest 自动化框架
作者: G-Tester
自我介绍: hello, world !!! I am a G-Tester. 你好，世界! 我是一个贯彻Google测试之道的测试者
框架版本: Sister -- 俗称小姐姐版, 让小姐姐也能快乐的玩耍
框架宗旨: 追求轻量简洁, 开箱即用
框架特点:
1. 整合了 Web自动化, 接口自动化; 通过开关变量可以开启对应的自动化框架; 多个自动化框架可以同时运行
2. web自动化中的元素定位统一使用xpath; id定位的xpath写法: `//*[@id="xxxx"]`; class定位的xpath写法: `//*[@class="xxxx"]`
3. 路径写法统一从根目录开始写, 示例: `testcases/test_api/yaml/common.yaml`
注意事项:
1. allure 测试报告需要手工自定义
2. token 的过期时间需要从响应体中获取
"""

# 默认根目录为当前文件所在的目录
ROOT_DIR = os.path.dirname(__file__)

if __name__ == '__main__':
    pytest.main()
    # 生成 allure 测试报告, allure 测试报告需要手工自定义格式
    cmd = r"allure generate ./allure_reports/tmp  -o ./allure_reports/html --clean"
    os.system(cmd)
