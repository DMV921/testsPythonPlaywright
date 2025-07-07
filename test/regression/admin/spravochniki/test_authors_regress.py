import allure
import pytest
from playwright.sync_api import Page
from page.admin.authors.authors_page import AuthorsPage
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
def authors_page(page: Page):
    return AuthorsPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/smoke/test_auth_logout.py::TestSmoke --browser=firefox --headless
@allure.epic("Тестирование справочника Авторы")
class TestAuthors:

    @allure.title("Добавление автора в справочник Авторы")
    @pytest.mark.regress
    def test_add_author(self, base_page, login_page, main_page, login_logout_page, authors_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        authors_page.open_authors_page()
        authors_page.add_author()
        message = authors_page.get_message_box()
        assert "Запись успешно создана" in message

    @allure.title("Изменение автора в справочнике Авторы")
    @pytest.mark.regress
    def test_change_author(self, base_page, login_page, main_page, login_logout_page, authors_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        authors_page.open_authors_page()
        authors_page.change_author()
        message = authors_page.get_message_box()
        assert "Запись успешно изменена" in message

    @allure.title("Удаление автора в справочнике Авторы")
    @pytest.mark.regress
    def test_delete_author(self, base_page, login_page, main_page, login_logout_page, authors_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        authors_page.open_authors_page()
        authors_page.delete_author()
        message = authors_page.get_message_box()
        assert "Запись успешно удалена" in message

