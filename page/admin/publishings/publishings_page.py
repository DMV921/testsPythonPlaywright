import time
import allure
from page.admin.authors.authors_locators import AUTHORS_PAGE_BUTTON
from page.base_page import BasePage
from web_page import WebPage

class PublishingsPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в раздел Издательства")
    def open_publishings_page(self):
        self.select_spravochnik("Издательства")

    @allure.step("Добавление издательства")
    def add_publishing(self):
        self.press_button("Добавить")
        self.fill_field("Издательство", "Тестовое издательство")
        self.press_button("Сохранить")

    @allure.step("Изменение издательства")
    def change_publishing(self):
        self.fill_search_field("Тестовое издательство")
        self.select_from_dropdown_list_change_delete("Изменить", "Тестовое издательство")
        self.fill_field("Издательство", "Тестовое издательство Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление издательства")
    def delete_publishing(self):
        self.fill_search_field("Тестовое издательство Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "Тестовое издательство Изменение")
        self.press_button("Удалить")
