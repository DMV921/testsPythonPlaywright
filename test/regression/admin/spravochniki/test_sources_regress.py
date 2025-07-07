import allure
import pytest
from playwright.sync_api import Page
from page.admin.sources.sources_page import SourcesPage
from page.base_page import BasePage
from page.bookfund.bookfund_data import MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22
from page.bookfund.bookfund_page import MainPage
from page.login.login_data import ROLE_DROPDOWN_ADMIN_SYS, PERSON_DROPDOWN_KUZNECOVA
from page.login.login_page import AuthLoginPage

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def login_page(page: Page):
    return AuthLoginPage(page)

@pytest.fixture
def main_page(page: Page):
    return MainPage(page)

@pytest.fixture
def sources_page(page: Page):
    return SourcesPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/smoke/test_auth_logout.py::TestSmoke --browser=firefox --headless
@allure.epic("Тестирование справочника Источники поступления")
class TestSources:

    @allure.title("Добавление источника в справочник Источники поступления")
    @pytest.mark.regress
    def test_add_sources(self, base_page, login_page, main_page, login_logout_page, sources_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        sources_page.open_sources_page()
        sources_page.add_sources()
        message = sources_page.get_message_box()
        assert "Запись успешно создана" in message

    @allure.title("Изменение издательства в справочнике Издательства")
    @pytest.mark.regress
    def test_change_sources(self, base_page, login_page, main_page, login_logout_page, sources_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        sources_page.open_sources_page()
        sources_page.change_sources()
        message = sources_page.get_message_box()
        assert "Запись успешно изменена" in message

    @allure.title("Удаление издательства в справочнике Издательства")
    @pytest.mark.regress
    def test_delete_sources(self, base_page, login_page, main_page, login_logout_page, sources_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        sources_page.open_sources_page()
        sources_page.delete_sources()
        message = sources_page.get_message_box()
        assert "Запись успешно удалена" in message

