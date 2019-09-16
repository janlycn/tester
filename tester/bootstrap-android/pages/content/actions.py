# Content 页

from pages.page_base import PageBase
from pages.content.elements import ContentElements


class ContentActions(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver)
        self.elements = ContentElements(driver)

    def click_storage_element(self):
        self.elements.storage_element().click()
        return True
