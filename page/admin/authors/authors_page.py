import time
import allure
from page.admin.authors.authors_locators import AUTHORS_PAGE_BUTTON
from page.base_page import BasePage
from web_page import WebPage

class AuthorsPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в раздел Администрирование")
    def open_authors_page(self):
        self.base.actions.click(AUTHORS_PAGE_BUTTON)

    @allure.step("Добавление автора")
    def add_author(self):
        self.press_button("Добавить")
        self.fill_field("Автор(-ы)", "Тестовый автор UI")
        self.press_button("Сохранить")

    @allure.step("Изменение автора")
    def change_author(self):
        self.fill_search_field("Тестовый автор UI")
        self.select_from_dropdown_list_change_delete("Изменить", "Тестовый автор UI")
        self.fill_field("Автор(-ы)", "Тестовый автор UI Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление автора")
    def delete_author(self):
        self.fill_search_field("Тестовый автор UI Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "Тестовый автор UI Изменение")
        self.press_button("Удалить")
