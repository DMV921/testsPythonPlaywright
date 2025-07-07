from playwright.sync_api import Page
from config.utils.logger import get_logger
from config.actions import ActionPage
from config.asserts import AssertPage
from config.utils.reporter import ReportPage
from config.utils.helpers import HelpPage


# Константы страницы:
BASE_URL = "https://edulib-general-2.edu.bars.group"

class BasePage:

    def __init__(self, page: Page):
        """Инициализация страницы браузера и зависимости."""
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
        self.actions = ActionPage(page)
        self.asserts = AssertPage(page)
        self.report = ReportPage(page)
        self.help = HelpPage(page)


