# 首页测试用例例子

import pytest

from appium import webdriver
from actions.actions_home import ActionsHome

from utils import index

# appium基础能力配置
ANDROID_BASE_CAPS = {
    # 平台
    'platformName': 'Android',
    # 平台版本
    'platformVersion': '4.4.2',
    # 自动化驱动
    'automationName': 'UIAutomator1',
    # 设备，这里是夜神，可使用 adb devices 查看
    'deviceName': '127.0.0.1:62001 device',
    # 启动 app 包名
    'appPackage': 'io.appium.android.apis',
    # 启动 activity 名
    'appActivity': 'io.appium.android.apis.ApiDemos',
    # 结束后保留状态
    'noReset': True
}


class TestPageHome():

    # 函数级 fixture，每个函数执行，执行结果作函数 driver 参数传入
    @pytest.fixture(scope='function')
    def driver(self):
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=ANDROID_BASE_CAPS
        )

        # 隐式等待
        driver.implicitly_wait(10)
        return driver

    def test_click_home_content(self, driver):
        page_content = ActionsHome(driver).click_content()
        assert page_content.storage_element
