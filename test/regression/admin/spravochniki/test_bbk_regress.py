import allure
import pytest
from playwright.sync_api import Page
from page.admin.bbk.bbk_page import BBKPage
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
def bbk_page(page: Page):
    return BBKPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/smoke/test_auth_logout.py::TestSmoke --browser=firefox --headless
@allure.epic("Тестирование справочника Разделы ББК")
class TestBBK:

    # === Основные разделы ===
    @allure.title("Добавление раздела в справочник Разделы ББК")
    @pytest.mark.regress
    def test_add_bbk(self, base_page, login_page, main_page, login_logout_page, bbk_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        bbk_page.open_bbk_page()
        bbk_page.add_bbk()
        message = bbk_page.get_message_box()
        assert "Запись успешно создана" in message

    @allure.title("Изменение раздела в справочнике Разделы ББК")
    @pytest.mark.regress
    def test_change_bbk(self, base_page, login_page, main_page, login_logout_page, bbk_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        bbk_page.open_bbk_page()
        bbk_page.change_bbk()
        message = bbk_page.get_message_box()
        assert "Запись успешно изменена" in message

    # === Дочерние разделы ===
    @allure.title("Добавление дочерней записи в справочник Разделы ББК")
    @pytest.mark.regress
    def test_add_child_bbk(self, base_page, login_page, main_page, login_logout_page, bbk_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        bbk_page.open_bbk_page()
        bbk_page.add_child_bbk()
        message = bbk_page.get_message_box()
        assert "Запись успешно создана" in message

    @allure.title("Изменение дочерней записи в справочник Разделы ББК")
    @pytest.mark.regress
    def test_change_child_bbk(self, base_page, login_page, main_page, login_logout_page, bbk_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        bbk_page.open_bbk_page()
        bbk_page.change_child_bbk()
        message = bbk_page.get_message_box()
        assert "Запись успешно изменена" in message

    @allure.title("Удаление дочерней записи в справочник Разделы ББК")
    @pytest.mark.regress
    def test_delete_child_bbk(self, base_page, login_page, main_page, login_logout_page, bbk_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        bbk_page.open_bbk_page()
        bbk_page.delete_child_bbk()
        message = bbk_page.get_message_box()
        assert "Запись успешно удалена" in message

    # === Основные разделы ===
    @allure.title("Удаление раздела в справочнике Разделы ББК")
    @pytest.mark.regress
    def test_delete_bbk(self, base_page, login_page, main_page, login_logout_page, bbk_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        bbk_page.open_bbk_page()
        bbk_page.delete_bbk()
        message = bbk_page.get_message_box()
        assert "Запись успешно удалена" in message

