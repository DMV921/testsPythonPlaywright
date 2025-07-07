import time
import allure
from page.admin.authors.authors_locators import AUTHORS_PAGE_BUTTON
from page.base_page import BasePage
from web_page import WebPage

class SourcesPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в раздел Источники поступления")
    def open_sources_page(self):
        self.select_spravochnik("Источники поступления")

    @allure.step("Добавление Источника поступления")
    def add_sources(self):
        self.press_button("Добавить")
        self.fill_field("Источник поступления", "Тестовый источник поступления")
        self.press_button("Сохранить")

    @allure.step("Изменение источника поступления")
    def change_sources(self):
        self.fill_search_field("Тестовый источник поступления")
        self.select_from_dropdown_list_change_delete("Изменить", "Тестовый источник поступления")
        self.fill_field("Источник поступления", "Тестовый источник поступления Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление источника поступления")
    def delete_sources(self):
        self.fill_search_field("Тестовый источник поступления Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "Тестовый источник поступления Изменение")
        self.press_button("Удалить")
