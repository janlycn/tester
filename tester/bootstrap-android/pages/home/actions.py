# 首页

from pages.page_base import PageBase
from pages.home.elements import HomeElements
from pages.content.elements import ContentElements


class HomeActions(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)
        self.homeElements = HomeElements(driver)

    def click_content(self):
        self.homeElements.content_element().click()
        return ContentElements(self.driver)
