import allure
from page.base_page import BasePage
from web_page import WebPage

class ExampleTypesPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в раздел Типы библиотечных экземпляров")
    def open_example_types_page(self):
        self.select_spravochnik("Типы библиотечных экземпляров")

    @allure.step("Добавление типа библиотечного экземпляра")
    def add_example_types(self):
        self.press_button("Добавить")
        self.fill_field("Наименование", "Тестовый тип библиотечного экземпляра")
        self.select_from_dropdown("Тип", "Печатные")
        self.press_button("Сохранить")

    @allure.step("Изменение типа библиотечного экземпляра")
    def change_example_types(self,search_value, example_types_type):
        self.fill_search_field(search_value)
        self.select_from_dropdown_list_change_delete("Изменить", search_value)
        self.fill_field("Наименование", "Измененный тестовый тип библиотечного экземпляра")
        self.select_from_dropdown("Тип", example_types_type)
        self.press_button("Сохранить")

    @allure.step("Удаление типа библиотечного экземпляра")
    def delete_example_types(self):
        self.fill_search_field("Измененный тестовый тип библиотечного экземпляра")
        self.select_from_dropdown_list_change_delete("Удалить", "Измененный тестовый тип библиотечного экземпляра")
        self.press_button("Удалить")
