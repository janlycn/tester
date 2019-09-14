# 首页

from pages.page_base import PageBase


class PageHome(PageBase):

    # def __init__(self, driver):
    #     PageBase.__init__(self, driver)

    def content_element(self):
        return self.driver.find_element_by_accessibility_id('Content')
