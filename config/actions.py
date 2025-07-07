from playwright.sync_api import Page
from config.utils.logger import get_logger
from playwright.sync_api import TimeoutError


class ActionPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        # Переходит на указанный URL
        self.logger.info(f"Переход по URL: {url}")
        self.page.goto(url)

    def click(self, locator):
        # Кликает по элементу с заданным локатором
        if isinstance(locator, str):
            locator = self.page.locator(locator)

        self.scroll_to_element(locator, smooth=True)

        # Ждём, пока элемент будет видим и прикреплён к DOM
        locator.wait_for(state="visible", timeout=10000)
        locator.wait_for(state="attached", timeout=10000)

        self.logger.info(f"Клик по элементу: {locator}")
        locator.click()

    def fill(self, locator, text):
        # Заполняет поле с заданным локатором текстом
        self.logger.info(f"Заполнение поля {locator} текстом: {text}")
        self.page.fill(locator, text)

    # def select_option(self, locator, label_text):
    #     # Выбирает значение из селектора с выпадающим списком
    #     self.logger.info(f"Выбор значения '{label_text}' в селекторе {locator}")
    #     self.page.select_option(locator, label=label_text)

    def select_option(self, locator, label_text):
        self.logger.info(f"Выбор значения '{label_text}' в селекторе {locator}")

        # Ждём, пока селектор существует (сам select)
        self.page.wait_for_selector(locator, timeout=10000)

        # Выполняем выбор без ожидания visibility для option
        self.page.select_option(locator, label=label_text)

    def wait_for_url(self, url):
        # Ждёт появления заданного URL
        self.logger.info(f"Ожидание загрузки URL: {url}")
        self.page.wait_for_url(url)

    def hover(self, locator):
        # Наводит курсор мыши на элемент
        self.logger.info(f"Наведение на элемент: {locator}")
        self.page.hover(locator)

    def get_text(self, locator):
        # Получает текстовое содержимое элемента
        text = self.page.text_content(locator)
        self.logger.info(f"Получен текст из {locator}: {text}")
        return text

    def is_visible(self, locator):
        # Проверяет, виден ли элемент на странице
        visible = self.page.is_visible(locator)
        self.logger.info(f"Элемент {locator} видим: {visible}")
        return visible

    def is_enabled(self, locator):
        # Проверяет, активен ли элемент (не disabled)
        enabled = self.page.is_enabled(locator)
        self.logger.info(f"Элемент {locator} активен: {enabled}")
        return enabled

    def wait_for_selector(self, locator, timeout: float):
        # Ждёт появления элемента с заданным локатором
        self.logger.info(f"Ожидание селектора {locator} в течение {timeout} сек.")
        self.page.wait_for_selector(locator, timeout=timeout * 1000)

    def wait(self, timeout: float):
        # Ждёт
        self.logger.info(f"Ожидание {timeout} сек.")
        self.page.wait_for_timeout(timeout * 1000)

    def wait_load_all(self, load_opt):
        # Ждёт загрузки, варианты: Только DOM без ресов "domcontentloaded", полная загрузка всего "load", отсутствие сетевых запросов дольше 500 мс "networkidle"
        self.logger.info(f"Ожидание загрузки страницы")
        self.page.wait_for_load_state(load_opt)

    def wait_load_all_js(self):
        self.logger.info(f"Можно использовать JavaScript-способ: ждем, пока DOM полностью загрузится")
        self.page.wait_for_function("document.readyState === 'complete'")

    def scroll_to_element(self, element, timeout: int = 30000, smooth: bool = False):
        """
        Скроллит к переданному элементу (Playwright Locator).

        :param element: Locator-элемент
        :param timeout: таймаут в мс
        :param smooth: использовать плавный скролл
        """
        try:
            element.wait_for(state="attached", timeout=timeout)
            element.wait_for(state="visible", timeout=timeout)
            if smooth:
                handle = element.element_handle(timeout=timeout)
                if handle:
                    self.page.evaluate(
                        "el => el.scrollIntoView({behavior: 'smooth', block: 'center'})",
                        handle
                    )
                else:
                    raise Exception("Не удалось получить element_handle для scroll_to_element")
            else:
                element.scroll_into_view_if_needed(timeout=timeout)
        except TimeoutError:
            self.page.wait_for_timeout(1000)
            raise Exception("Элемент не найден или не прокручен!")



