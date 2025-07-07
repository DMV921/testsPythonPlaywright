import time
import allure
from page.base_page import BasePage, BASE_URL
from page.bookfund.bookfund_data import BOOKFUND_PAGE_URL
from page.bookfund.bookfund_locators import HEADER_MENU_LOCATOR, LOGOUT_BUTTON_LOCATOR, MainPageLocators, \
    CHOICE_ORGANISATION_BUTTON_LOCATOR, ORGANISATION_SELECTOR_LOCATOR, ORGANISATION_SELECTOR_SAVE_BUTTON, \
    ADMIN_PAGE_BUTTON_LOCATOR, SCHOOL_DROPDOWN_INPUT
from web_page import WebPage


class MainPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = WebPage(page)

    @allure.step("Выбор школы в виджете Организации")
    def select_schooldropdown_main_page(self, text:str):
        self.base.actions.wait_for_selector(CHOICE_ORGANISATION_BUTTON_LOCATOR, 10)
        self.base.actions.click(CHOICE_ORGANISATION_BUTTON_LOCATOR)
        self.base.actions.wait_load_all_js()
        self.base.actions.wait_for_selector(ORGANISATION_SELECTOR_LOCATOR, 10)
        self.base.actions.click(ORGANISATION_SELECTOR_LOCATOR)
        self.base.actions.fill(SCHOOL_DROPDOWN_INPUT, text)
        self.base.actions.wait_for_selector(MainPageLocators.SCHOOL_SELECTOR_LOCATOR(text), 10)
        self.base.actions.click(MainPageLocators.SCHOOL_SELECTOR_LOCATOR(text))
        # self.base.select_from_dropdown("Список доступных организаций",'МБОУ "СОШ № 22"', )
        self.base.actions.click(ORGANISATION_SELECTOR_SAVE_BUTTON)
        self.base.actions.wait_for_url(BOOKFUND_PAGE_URL)
        self.close_toast_by_text("Организация успешно изменена")

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.base.actions.click(HEADER_MENU_LOCATOR)
        self.base.actions.click(LOGOUT_BUTTON_LOCATOR)
        self.base.actions.wait_load_all_js()
        self.base.actions.wait(1)

    @allure.step("Переход в раздел Администрирование")
    def open_admin_page(self):
        self.base.actions.click(ADMIN_PAGE_BUTTON_LOCATOR)

    @allure.step("Переход в реестр")
    def open_registry_page(self, text: str):
        self.base.actions.click(MainPageLocators.OPEN_REGISTRY_LOCATOR(text))

