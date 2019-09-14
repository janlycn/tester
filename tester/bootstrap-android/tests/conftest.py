
import pytest
import copy
import settings

from appium import webdriver


# 函数级 fixture，每个函数执行，执行结果作函数 driver 参数传入
@pytest.fixture(scope='module')
def driver(request):
    caps = copy.copy(settings.ANDROID_BASE_CAPS)

    driver = webdriver.Remote(
        command_executor=settings.COMMAND_EXECUTOR,
        desired_capabilities=caps
    )

    def fin():
        # report_to_sauce(driver.session_id)
        # take_screenshot_and_logcat(driver, device_logger, calling_request)
        driver.quit()

    # 测试结束后执行
    request.addfinalizer(fin)

    # 隐式等待
    driver.implicitly_wait(10)
    return driver
