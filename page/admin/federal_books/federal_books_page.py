import time
import allure
from page.admin.authors.authors_locators import AUTHORS_PAGE_BUTTON
from page.base_page import BasePage
from web_page import WebPage

class FederalBooksPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в раздел Федеральный перечень учебников")
    def open_federal_books_page(self):
        self.select_spravochnik("Федеральный перечень учебников")

    @allure.step("Импорт в Федеральный перечень учебников")
    def import_federal_books(self):
        self.press_button("Импорт")
        self.test_upload_file("Файл", "page/admin/federal_books/files/Федеральный перечень для загрузки.xlsx")
        self.press_button("Импортировать")

