
import pytest
import copy
import settings

from appium import webdriver


class TBase():

    # 函数级 fixture，每个函数执行，执行结果作函数 driver 参数传入
    @pytest.fixture(scope='function')
    def driver(self):
        caps = copy.copy(settings.ANDROID_BASE_CAPS)

        driver = webdriver.Remote(
            command_executor=settings.COMMAND_EXECUTOR,
            desired_capabilities=caps
        )

        # 隐式等待
        driver.implicitly_wait(10)
        return driver
