import time
import allure
from playwright.sync_api import expect
from page.base_page import BasePage, BASE_URL
import os
from pathlib import Path
from page.bookfund.bookfund_data import BOOKFUND_PAGE_URL
from page.login.login_data import *
from page.login.login_locators import *

"""Содержит методы для наиболее встречающихся элементов"""
class WebPage(BasePage):
    """Шаблон Page Object"""

    def __init__(self, page):
        super().__init__(page)
        self.base = BasePage(page)

    @allure.step("Нажать на кнопку: {button_name}")
    def press_button(self, button_name: str, element_count: int = 1):
        """
        Нажимает на кнопку с заданным текстом и логирует шаг в Allure.
        :param button_name: Текст кнопки.
        :param element_count: Индекс кнопки (начинается с 1).
        """
        xpath = f"(//button//div[text() = '{button_name}'])[{element_count}]"

        # Ждём, пока кнопка появится и станет кликабельной
        self.page.wait_for_selector(xpath, state="visible", timeout=5000)
        self.page.wait_for_selector(xpath, state="attached", timeout=5000)

        # Кликаем по кнопке
        self.base.actions.click(xpath)

    @allure.step("Выбор справочника {button_name}")
    def select_spravochnik(self, button_name: str, element_count: int = 1):
        """
        Нажимает на кнопку с заданным текстом и логирует шаг в Allure.
        :param button_name: Текст кнопки.
        :param element_count: Индекс кнопки (начинается с 1).
        """
        xpath = f"(//div[text() = '{button_name}'])"

        # Ждём, пока кнопка появится и станет кликабельной
        self.page.wait_for_selector(xpath, state="visible", timeout=5000)
        self.page.wait_for_selector(xpath, state="attached", timeout=5000)

        # Кликаем по кнопке
        self.page.click(xpath)

    @allure.step("Заполнить поле '{field_name}' значением '{value}'")
    def fill_field(self, field_name: str, value: str, press_enter: bool = False):
        xpath = (
            f"//div[contains(@class, 'plex-typography') and text()='{field_name}']"
            f"/ancestor::*[contains(@class, 'plex-field')]"
            f"//input[contains(@class, 'plex-field-input')]"
        )
        locator = self.page.locator(xpath)
        locator.wait_for(state="visible")
        locator.fill(value)
        if press_enter:
            locator.press("Enter")

    # @allure.step("Получение текста из всплывающего сообщения (toast)")
    # def get_message_box(self) -> str:
    #     locator = "div > div.plex-toast__content > div"
    #     self.page.wait_for_selector(locator, state="visible")
    #     message = self.page.locator(locator).inner_text()
    #     return message

    @allure.step("Получение текста из всплывающего сообщения (toast)")
    def get_message_box(self) -> str:
        locator = f"//div[contains(@class, 'plex-typography') and contains(@class, 'plex-toast__text')]"
        self.page.wait_for_selector(locator, state="visible")
        message = self.page.locator(locator).inner_text()
        return message

    def wait_for_message(self, expected_text, timeout=10):
        import time
        selector = "div > div.plex-toast__content > div"
        end_time = time.time() + timeout
        while time.time() < end_time:
            elements = self.page.query_selector_all(selector)
            for el in elements:
                text = el.text_content() or ""
                if expected_text in text.strip():
                    return text.strip()  # возвращаем текст найденного сообщения
            time.sleep(0.5)
        raise AssertionError(f"Сообщение с текстом '{expected_text}' не появилось за {timeout} секунд")

    @allure.step("Выбор действия '{button_name}' из дропдауна для поля '{field}'")
    def select_from_dropdown_list_change_delete(self, button_name: str, field: str):
        dropdown_icon_xpath = (
            f"//div[contains(@class, 'plex-typography') and text()='{field}']"
            f"/ancestor::*[contains(@class, 'plex-grid-row')]"
            f"//*[@href = '#icon-plex-menu-meatballs-outline']/.."
        )
        button_xpath = f"//div[@class='plex-menu-item__body']//div[text()='{button_name}']"

        dropdown_locator = self.page.locator(dropdown_icon_xpath)
        button_locator = self.page.locator(button_xpath)

        dropdown_locator.wait_for(state="visible", timeout=5000)

        # Ожидаем появления и кликаем по иконке дропдауна
        self.base.actions.scroll_to_element(dropdown_locator, smooth=True)
        self.page.locator(dropdown_icon_xpath).focus()
        self.page.locator(dropdown_icon_xpath).hover()
        self.page.wait_for_selector(dropdown_icon_xpath, state="visible")
        self.base.actions.click(dropdown_icon_xpath)

        # Ожидаем и кликаем по нужному элементу в дропдауне
        button_locator.wait_for(state="visible", timeout=5000)
        self.base.actions.scroll_to_element(button_locator, smooth=True)
        self.page.locator(button_xpath).focus()
        self.page.wait_for_selector(button_xpath, state="visible")
        self.base.actions.click(button_xpath)

    @allure.step("Ввод в поле поиска: {value}")
    def fill_search_field(self, value: str, press_enter: bool = False):
        xpath = "//div[contains(@class, 'search-input')]//input[not(ancestor-or-self::*[contains(@style, 'display: none')])]"
        locator = self.page.locator(xpath).first
        locator.wait_for(state="visible", timeout=5000)
        self.base.actions.scroll_to_element(locator, smooth=True)
        locator.focus()
        locator.hover()
        locator.fill(value)
        if press_enter:
            locator.press("Enter")
        results_locator = self.page.locator("//div[contains(@class, 'plex-grid-cell-content')]")
        results_locator.first.wait_for(timeout=10000)

    #Ввод в поле поиска в разделах ББК и УДК
    @allure.step("Ввод в поле поиска: {value}")
    def fill_search_field_bbk_udc(self, value: str, press_enter: bool = False):
        xpath = "//div[contains(@class, 'plex-field__input')]//input[not(ancestor-or-self::*[contains(@style, 'display: none')])]"
        locator = self.page.locator(xpath).first
        locator.wait_for(state="visible", timeout=5000)
        self.base.actions.scroll_to_element(locator, smooth=True)
        locator.focus()
        locator.hover()
        locator.fill(value)
        if press_enter:
            locator.press("Enter")
        results_locator = self.page.locator(
            "//div[contains(@class, 'plex-grid-cell-content')]")  # или другой, если список другой
        results_locator.first.wait_for(timeout=10000)

    # Открытие дочерней записи в разделах ББК и УДК
    @allure.step("Нажать на кнопку: {section_name}")
    def open_bbk_udc_child_section(self, section_name: str):
        """
        Нажимает на кнопку с заданным текстом и логирует шаг в Allure.
        :param button_name: Текст кнопки.
        :param element_count: Индекс кнопки (начинается с 1).
        """
        xpath = f"//div[contains(@class, 'plex-typography') and text()='{section_name}']/ancestor::*[contains(@class, 'last-node')]//*[@href = '#icon-plex-system-triangle-right-s-solid']"
        locator = self.page.locator(xpath).first

        # Ждём, пока кнопка появится и станет кликабельной
        self.page.wait_for_selector(xpath, state="visible", timeout=5000)
        self.page.wait_for_selector(xpath, state="attached", timeout=5000)

        # Кликаем по кнопке
        self.base.actions.click(locator)

    @allure.step("Выбрать из выпадающего списка '{dropdown_label}' значение '{option_text}'")
    def select_from_dropdown(self, dropdown_label: str, option_text: str):
        # Открываем дропдаун
        self.open_dropdown(dropdown_label)
        # Кликаем по нужной опции
        option_locator = f"//div[contains(@class, 'plex-menu-item__text') and text()='{option_text}']"
        self.base.actions.wait_for_selector(option_locator, timeout=10)
        self.base.actions.click(option_locator)

    @allure.step("Открыть выпадающий список '{dropdown_label}'")
    def open_dropdown(self, dropdown_label: str):
        # Находим и кликаем по триггеру дропдауна
        dropdown_trigger_xpath = (
            f"//div[contains(@class, 'plex-typography') and text()='{dropdown_label}']"
            f"/ancestor::*[contains(@class, 'plex-field')]"
            f"//input[contains(@class, 'plex-field-input')]"
        )
        self.base.actions.click(dropdown_trigger_xpath)

    def set_checkbox_by_label(self, label_text: str, check: bool):
        # Находим чекбокс по тексту label'а
        checkbox = self.page.locator(
            f"//div[contains(@class, 'plex-typography') and text()='{label_text}']"
            f"/ancestor::*[contains(@class, 'plex-checkbox')]//input[@type='checkbox']"
        )

        # Приводим к нужному состоянию
        if check:
            checkbox.check(force=True)
        else:
            checkbox.uncheck(force=True)

    @allure.step("Перенос файла в облась для загрузки")
    def drag_and_drop_upload(self, selector: str, file_path: str, mime_type: str = "application/octet-stream",
                             use_xpath=False):
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        locator = self.page.locator(f"xpath={selector}" if use_xpath else selector)
        locator.wait_for(timeout=5000)

        with open(file, "rb") as f:
            file_bytes = f.read()

        print(f"📁 Загружаем файл: {file.name} ({mime_type})")

        locator.evaluate(
            """(target, args) => {
                const file = new File([new Uint8Array(args.bytes)], args.name, { type: args.mime });
                const dt = new DataTransfer();
                dt.items.add(file);

                for (const eventName of ['dragenter', 'dragover', 'drop']) {
                    const event = new DragEvent(eventName, {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dt
                    });
                    target.dispatchEvent(event);
                }
            }""",
            {
                "name": file.name,
                "mime": mime_type,
                "bytes": list(file_bytes),
            }
        )

    @allure.step("Импорт файла")
    def test_upload_file(self, field_name, relative_path):
        # Абсолютный путь к папке с текущим скриптом (federal_books)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Строим путь к файлу в подпапке files
        parts = relative_path.split('/')
        file_path = os.path.join(current_dir, *parts)

        print(f"Пытаемся загрузить файл по пути: {file_path}")
        print(f"Файл существует? {os.path.exists(file_path)}")

        self.drag_and_drop_upload(
            selector=f"//div[contains(@class, 'plex-typography') and text()='{field_name}']/ancestor::*[contains(@class, 'file-uploader')]//div[contains(@class, 'dropdown-place__description')]",
            file_path=str(file_path),
            mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_xpath=True
        )

        # поиск нужной строки по значениям //div[contains(@class, 'plex-grid-row') and .//div[contains(@class, 'plex-typography') and text()='Тестовая новая'] and .//div[contains(@class, 'plex-typography') and text()='язык'] and .//div[contains(@class, 'plex-typography') and text()='25.04.2027']  and .//div[contains(@class, 'plex-typography') and text()='Да']]

    @allure.step("Поиск строки таблицы с {values}")
    def get_table_row_by_values(self, *values: str):
        count = len(values)

        # Собираем XPath
        xpath = "//div[contains(@class, 'plex-grid-row')"
        for val in values:
            xpath += f" and .//div[contains(@class, 'plex-typography') and text()='{val}']"
        xpath += "]"

        try:
            # Ждём появления строки и её видимости
            self.page.wait_for_selector(xpath, timeout=5000)
            row = self.page.locator(xpath)
            row.wait_for(state="visible", timeout=5000)
            return row
        except Exception:
            # Прикрепляем текст ожидаемых значений в Allure-отчёт
            allure.attach(
                body="\n".join(values),
                name="Ожидаемые значения строки",
                attachment_type=allure.attachment_type.TEXT
            )
            return None

    @allure.step("Выбор сортировки '{button_name}' из дропдауна сортировок ")
    def select_from_dropdown_sort(self, button_name: str):
        dropdown_icon_xpath = (
            "//div[contains(@class, ' table-sort-popup__button')]"
        )
        button_xpath = f"//div[@class='plex-menu-item__body']//div[text()='{button_name}']"

        dropdown_locator = self.page.locator(dropdown_icon_xpath)
        button_locator = self.page.locator(button_xpath)

        dropdown_locator.wait_for(state="visible", timeout=5000)

        # Ожидаем появления и кликаем по иконке дропдауна
        self.base.actions.scroll_to_element(dropdown_locator, smooth=True)
        self.page.locator(dropdown_icon_xpath).focus()
        self.page.locator(dropdown_icon_xpath).hover()
        self.page.wait_for_selector(dropdown_icon_xpath, state="visible")
        self.base.actions.click(dropdown_icon_xpath)

        # Ожидаем и кликаем по нужному элементу в дропдауне
        button_locator.wait_for(state="visible", timeout=5000)
        self.base.actions.scroll_to_element(button_locator, smooth=True)
        self.page.locator(button_xpath).focus()
        self.page.wait_for_selector(button_xpath, state="visible")
        self.base.actions.click(button_xpath)

    @allure.step("Выбор действия '{button_name}' из дропдауна для строки с значениями: {values}")
    def select_from_dropdown_by_row_values(self, button_name: str, *values: str):
        if not values:
            raise ValueError("Не переданы значения для поиска строки таблицы.")

        # Строим XPath для строки по значениям
        row_xpath = "//div[contains(@class, 'plex-grid-row')"
        for val in values:
            row_xpath += f" and .//div[contains(@class, 'plex-typography') and text()='{val}']"
        row_xpath += "]"

        try:
            # Дожидаемся и получаем строку
            self.page.wait_for_selector(row_xpath, timeout=5000)
            row = self.page.locator(row_xpath)
            expect(row).to_be_visible()

            # Локатор для иконки дропдауна в этой строке
            dropdown_xpath = f"{row_xpath}//*[@href = '#icon-plex-menu-meatballs-outline']/.."
            dropdown_locator = self.page.locator(dropdown_xpath)

            dropdown_locator.wait_for(state="visible", timeout=5000)
            self.base.actions.scroll_to_element(dropdown_locator, smooth=True)
            dropdown_locator.focus()
            dropdown_locator.hover()
            self.page.wait_for_selector(dropdown_xpath, state="visible")
            self.base.actions.click(dropdown_xpath)

            # Локатор пункта дропдауна
            button_xpath = f"//div[@class='plex-menu-item__body']//div[text()='{button_name}']"
            button_locator = self.page.locator(button_xpath)

            button_locator.wait_for(state="visible", timeout=5000)
            self.base.actions.scroll_to_element(button_locator, smooth=True)
            button_locator.focus()
            self.page.wait_for_selector(button_xpath, state="visible")
            self.base.actions.click(button_xpath)

        except Exception as e:
            allure.attach(
                body="\n".join(values),
                name="Значения строки, в которой искался дропдаун",
                attachment_type=allure.attachment_type.TEXT
            )
            raise e

    @allure.step("Открыть окно выбора учебника'")
    def open_list(self, list_label: str):
        # Находим и кликаем по триггеру дропдауна
        dropdown_trigger_xpath = (
            f"//div[contains(@class, 'plex-typography') and text()='{list_label}']/ancestor::*[contains(@class, 'plex-field')]//*[@href = '#icon-plex-system-folder-open-regular']/.."
        )
        self.base.actions.click(dropdown_trigger_xpath)

    @allure.step("Выбор строки таблицы с значениями: {values}")
    def click_on_table(self, *values: str):
        if not values:
            raise ValueError("Не переданы значения для поиска строки таблицы.")

        # Формируем XPath строки с заданными значениями
        row_xpath = "//div[contains(@class, 'plex-grid-row')]"
        for val in values:
            row_xpath += f"[.//div[contains(@class, 'plex-typography') and text()='{val}']]"

        # Ждём и находим строку
        self.page.wait_for_selector(row_xpath, timeout=5000)
        row = self.page.locator(row_xpath)
        expect(row).to_be_visible()

        # Кликаем по найденной строке
        row.click()

    @allure.step("Нажать на кнопку: {button_name} (элемент #{element_count})")
    def click_cookie_button(self, button_name: str, element_count: int = 1):
        # Формируем XPath с индексом
        xpath = f"(//button//div[text()='{button_name}'])[{element_count}]"
        button = self.page.locator(xpath)
        button.wait_for(state="visible", timeout=5000)
        button.click()

    @allure.step("Ожидание, пока input будет содержать значение: '{expected_value}'")
    def wait_for_input_value_contains(self, expected_value: str, timeout: int = 10000, poll_interval: float = 0.5):
        xpath = f"//input[contains(@value, '{expected_value}')]"
        input_locator = self.page.locator(xpath)

        end_time = time.time() + timeout / 1000
        while time.time() < end_time:
            try:
                if input_locator.is_visible():
                    value = input_locator.input_value()
                    if expected_value in value:
                        return  # Успешно, значение найдено
            except Exception:
                pass
            time.sleep(poll_interval)

        # Если вышли из цикла - значит таймаут
        raise AssertionError(f"Input не содержит значение '{expected_value}' в течение {timeout}мс")

    def close_toast_by_text(self, expected_text: str, timeout: int = 5000):
        """
        Ищет всплывающее окно (toast) с текстом expected_text и закрывает его.
        Если окно не найдено в течение timeout, метод молча возвращает False.
        """
        try:
            toast_locator = self.page.locator(
                f"//div[contains(@class, 'plex-typography') and text()= '{expected_text}']"
                "/ancestor::*[contains(@class, 'plex-toast')]"
                "//*[@href='#icon-plex-system-cancel-s-outline']/.."
            )
            toast_locator.wait_for(state='visible', timeout=timeout)
            toast_locator.click()
            return True
        except TimeoutError:
            return False






















