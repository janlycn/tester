# 首页

from actions.actions_base import ActionBase
from pages.page_home import PageHome
from pages.page_content import PageContent


class ActionsHome(ActionBase):

    def __init__(self, driver):
        ActionBase.__init__(self, driver)
        self.page_home = PageHome(driver)

    def click_content(self):
        self.page_home.content_element().click()
        return PageContent(self.driver)
