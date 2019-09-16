# 首页测试用例例子

import pytest

# from tests.base import TBase
from pages.home.actions import HomeActions
from pages.content.actions import ContentActions
from utils import index


class TestPageHome():

    def test_click_home_content(self, cls_driver):
        result = HomeActions(cls_driver).click_content_element()
        assert result

    def test_click_content_storage(self, cls_driver):
        result = ContentActions(cls_driver).click_storage_element()
        assert result
