import allure
import pytest
from playwright.sync_api import Page
from page.admin.publishings.publishings_page import PublishingsPage
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
def publishings_page(page: Page):
    return PublishingsPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/smoke/test_auth_logout.py::TestSmoke --browser=firefox --headless
@allure.epic("Тестирование справочника Издательства")
class TestPublishings:

    @allure.title("Добавление автора в справочник Издательства")
    @pytest.mark.regress
    def test_add_publishing(self, base_page, login_page, main_page, login_logout_page, publishings_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        publishings_page.open_publishings_page()
        publishings_page.add_publishing()
        message = publishings_page.get_message_box()
        assert "Запись успешно создана" in message

    @allure.title("Изменение издательства в справочнике Издательства")
    @pytest.mark.regress
    def test_change_publishing(self, base_page, login_page, main_page, login_logout_page, publishings_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        publishings_page.open_publishings_page()
        publishings_page.change_publishing()
        message = publishings_page.get_message_box()
        assert "Запись успешно изменена" in message

    @allure.title("Удаление издательства в справочнике Издательства")
    @pytest.mark.regress
    def test_delete_publishing(self, base_page, login_page, main_page, login_logout_page, publishings_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        publishings_page.open_publishings_page()
        publishings_page.delete_publishing()
        message = publishings_page.get_message_box()
        assert "Запись успешно удалена" in message

