import time
import allure
from page.admin.authors.authors_locators import AUTHORS_PAGE_BUTTON
from page.base_page import BasePage
from web_page import WebPage

class UMKPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в раздел УМК")
    def open_umk_page(self):
        self.select_spravochnik("УМК")

    @allure.step("Добавление УМК")
    def add_umk(self, level_of_education, parallel, number_of_umk, set_checkbox):
        self.press_button("Добавить")
        self.select_from_dropdown("Ступень образования", level_of_education)
        self.select_from_dropdown("Параллель", parallel)
        self.fill_field("Количество УМК", number_of_umk)
        self.set_checkbox_by_label("Активен", set_checkbox)
        self.press_button("Сохранить")

    @allure.step("Изменение УМК")
    def change_umk(self, level_of_education, parallel, number_of_umk, set_checkbox, parallel_for_changing):
        self.select_from_dropdown_by_row_values("Изменить",  parallel_for_changing)
        self.select_from_dropdown("Ступень образования", level_of_education)
        self.select_from_dropdown("Параллель", parallel)
        self.fill_field("Количество УМК", number_of_umk)
        self.set_checkbox_by_label("Активен", set_checkbox)
        self.press_button("Сохранить")

    @allure.step("Удаление УМК")
    def delete_umk(self, *values: str):
        self.select_from_dropdown_by_row_values("Удалить", *values)
        self.press_button("Удалить")
