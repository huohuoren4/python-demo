import pytest


@pytest.fixture(scope="session", autouse=True)
def run():
    """欢迎使用 Autotest 自动化框架"""
    print("\n\033[32m欢迎使用 Autotest 自动化框架 (●'◡'●)\033[0m")
    print("\033[32m我们即将进行一次奇妙的旅行, are you ready?\033[0m\n")
    yield
    print("\n\033[32m我们已经到达旅途的终点,非常感谢你的参与（￣︶￣）↗\033[0m")



