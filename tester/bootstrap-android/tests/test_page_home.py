# 首页测试用例例子

import pytest

# from tests.base import TBase
from actions.actions_home import ActionsHome
from utils import index


class TestPageHome():

    def test_click_home_content(self, driver):
        page_content = ActionsHome(driver).click_content()
        assert page_content.storage_element
