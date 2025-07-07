import allure
from page.base_page import BasePage
from web_page import WebPage

class BBKPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в справочник Разделы ББК")
    def open_bbk_page(self):
        self.select_spravochnik("Разделы ББК")

    # === Основные разделы ===
    @allure.step("Добавление раздела ББК")
    def add_bbk(self):
        self.press_button("Добавить")
        self.fill_field("Код", "98")
        self.fill_field("Название", "Тестовый раздел ББК")
        self.press_button("Сохранить")

    @allure.step("Изменение раздела ББК")
    def change_bbk(self):
        self.fill_search_field_bbk_udc("Тестовый раздел ББК")
        self.select_from_dropdown_list_change_delete("Изменить", "98 Тестовый раздел ББК")
        self.fill_field("Код", "988")
        self.fill_field("Название", "Тестовый раздел ББК Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление раздела ББК")
    def delete_bbk(self):
        self.fill_search_field_bbk_udc("Тестовый раздел ББК Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "988 Тестовый раздел ББК Изменение")
        self.press_button("Удалить")

    # === Дочерние разделы ===
    @allure.step("Добавление дочерней записи в раздел ББК")
    def add_child_bbk(self):
        self.fill_search_field_bbk_udc("Тестовый раздел ББК Изменение")
        self.select_from_dropdown_list_change_delete("Добавить дочернюю запись", "988 Тестовый раздел ББК Изменение")
        self.fill_field("Код", "98888")
        self.fill_field("Название", "Тестовый дочерний раздел ББК")
        self.press_button("Сохранить")

    @allure.step("Изменение дочерней записи в разделе ББК")
    def change_child_bbk(self):
        self.fill_search_field_bbk_udc("Тестовый раздел ББК Изменение")
        self.open_bbk_udc_child_section("988 Тестовый раздел ББК Изменение")
        self.select_from_dropdown_list_change_delete("Изменить", "98888 Тестовый дочерний раздел ББК")
        self.fill_field("Код", "988881")
        self.fill_field("Название", "Тестовый дочерний раздел ББК Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление дочерней записи в разделе ББК")
    def delete_child_bbk(self):
        self.fill_search_field_bbk_udc("Тестовый раздел ББК Изменение")
        self.open_bbk_udc_child_section("988 Тестовый раздел ББК Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "988881 Тестовый дочерний раздел ББК Изменение")
        self.press_button("Удалить")