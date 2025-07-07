import time
import allure
from page.admin.authors.authors_locators import AUTHORS_PAGE_BUTTON
from page.base_page import BasePage
from web_page import WebPage

class LibRegistryPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Добавление издания в Библиотечный реестр")
    def add_lib_registry(self):
        self.click_cookie_button("Хорошо")
        self.press_button("Новое издание")
        self.open_list("Федеральный перечень")
        self.click_on_table("Часть 1: Мордкович А.Г., Семенов П.В.; Часть 2: Мордкович А.Г., Александрова А.Л., Мишустина Т.Н. идругие; подредакцией Мордковича А.Г.")
        self.press_button("Выбрать")
        self.wait_for_input_value_contains("Учебник, учебная литература")
        self.press_button("Сохранить")


