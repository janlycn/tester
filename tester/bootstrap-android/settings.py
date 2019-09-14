
# appium desired_capabilities
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

# appium command_executor
COMMAND_EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

# 测试集合
TEST_COLLECTION = {
    'home': {
       "pattern": 'test_page_home.py',
       "report": 'test_page_home.html'
    },
    'home_method': 'test_page_home.py::TestPageHome::test_click_home_content'
}
