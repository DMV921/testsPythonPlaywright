import time
import allure
from page.base_page import BasePage, BASE_URL
from page.bookfund.bookfund_data import BOOKFUND_PAGE_URL
from page.login.login_data import *
from page.login.login_locators import *


class AuthLoginPage(BasePage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Логин")
    def auth(self, role, person):
        self.base.actions.navigate(LOGIN_PAGE_URL)
        self.base.actions.select_option(REGION_DROPDOWN_LOCATOR, REGION_DROPDOWN_REPUBLIC_TATARSTAN)
        # self.page.wait_for_selector('#school-dropdown >> option:has-text(\'МБОУ "СОШ № 22"\')', timeout=10000)
        self.base.actions.wait(2)
        self.page.select_option(SCHOOL_DROPDOWN_LOCATOR, label=SCHOOL_DROPDOWN_MBOY_SOSH_22)
        self.base.actions.wait(2)
        self.base.actions.select_option(PERSON_DROPDOWN_LOCATOR, person)
        self.base.actions.wait(2)
        self.base.actions.select_option(ROLE_DROPDOWN_LOCATOR, role)
        self.base.actions.wait(5)
        self.base.actions.click(BUTTON_LOGIN_LOCATOR)
        self.base.actions.wait_for_url(BOOKFUND_PAGE_URL)
        self.base.actions.wait(7)
        self.base.actions.wait_load_all("load")
