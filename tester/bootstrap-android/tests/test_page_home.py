# 首页测试用例例子

import pytest

# from tests.base import TBase
from pages.home.actions import HomeActions
from utils import index


class TestPageHome():

    def test_click_home_content(self, driver):
        pageContent = HomeActions(driver).click_content()
        assert pageContent.storage_element
