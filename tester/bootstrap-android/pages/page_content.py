# content 页

from pages.page_base import PageBase


class PageContent(PageBase):

    # def __init__(self, driver):
    #     PageBase.__init__(self, driver)

    def storage_element(self):
        return self.driver.find_element_by_accessibility_id('Storage')
