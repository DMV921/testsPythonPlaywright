import allure
from page.base_page import BasePage
from web_page import WebPage

class UDCPage(WebPage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Переход в справочник Разделы УДК")
    def open_udc_page(self):
        self.select_spravochnik("Разделы УДК")

    # === Основные разделы ===
    @allure.step("Добавление раздела УДК")
    def add_udc(self):
        self.press_button("Добавить")
        self.fill_field("Код", "98")
        self.fill_field("Название", "Тестовый раздел УДК")
        self.press_button("Сохранить")

    @allure.step("Изменение раздела УДК")
    def change_udc(self):
        self.fill_search_field_bbk_udc("Тестовый раздел УДК")
        self.select_from_dropdown_list_change_delete("Изменить", "98 Тестовый раздел УДК")
        self.fill_field("Код", "988")
        self.fill_field("Название", "Тестовый раздел УДК Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление раздела УДК")
    def delete_udc(self):
        self.fill_search_field_bbk_udc("Тестовый раздел УДК Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "988 Тестовый раздел УДК Изменение")
        self.press_button("Удалить")

    # === Дочерние разделы ===
    @allure.step("Добавление дочерней записи в раздел УДК")
    def add_child_udc(self):
        self.fill_search_field_bbk_udc("Тестовый раздел УДК Изменение")
        self.select_from_dropdown_list_change_delete("Добавить дочернюю запись", "988 Тестовый раздел УДК Изменение")
        self.fill_field("Код", "98888")
        self.fill_field("Название", "Тестовый дочерний раздел УДК")
        self.press_button("Сохранить")

    @allure.step("Изменение дочерней записи в разделе УДК")
    def change_child_udc(self):
        self.fill_search_field_bbk_udc("Тестовый раздел УДК Изменение")
        self.open_bbk_udc_child_section("988 Тестовый раздел УДК Изменение")
        self.select_from_dropdown_list_change_delete("Изменить", "98888 Тестовый дочерний раздел УДК")
        self.fill_field("Код", "988881")
        self.fill_field("Название", "Тестовый дочерний раздел УДК Изменение")
        self.press_button("Сохранить")

    @allure.step("Удаление дочерней записи в разделе УДК")
    def delete_child_udc(self):
        self.fill_search_field_bbk_udc("Тестовый раздел УДК Изменение")
        self.open_bbk_udc_child_section("988 Тестовый раздел УДК Изменение")
        self.select_from_dropdown_list_change_delete("Удалить", "988881 Тестовый дочерний раздел УДК Изменение")
        self.press_button("Удалить")