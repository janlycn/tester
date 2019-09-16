# 首页

from pages.page_base import PageBase


class HomeElements(PageBase):

    def content_element(self):
        return self.driver.find_element_by_accessibility_id('Content')
