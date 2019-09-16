# 首页

from pages.page_base import PageBase
from pages.home.elements import HomeElements


class HomeActions(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)
        self.elements = HomeElements(driver)

    def click_content_element(self):
        self.elements.content_element().click()
        return True
