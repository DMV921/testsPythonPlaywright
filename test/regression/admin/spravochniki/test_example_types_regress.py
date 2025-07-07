import allure
import pytest
from playwright.sync_api import Page
from page.admin.example_types.example_types_page import ExampleTypesPage
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
def example_types_page(page: Page):
    return ExampleTypesPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/regression/admin/spravochniki/test_example_types_regress.py::TestExampleTypes --browser=firefox --headless
@allure.epic("Тестирование справочника Типы библиотечных экземпляров")
class TestExampleTypes:

    @allure.title("Добавление раздела в справочник Типы библиотечных экземпляров")
    @pytest.mark.regress
    def test_add_example_types(self, base_page, login_page, main_page, login_logout_page, example_types_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        example_types_page.open_example_types_page()
        example_types_page.add_example_types()
        message = example_types_page.get_message_box()
        assert "Запись успешно создана" in message

    @pytest.mark.parametrize(("search_value","example_types_type"), [
        ("Тестовый тип библиотечного экземпляра","Электронные (медиафайл и др)"),
        ("Измененный тестовый тип библиотечного экземпляра","Периодика"),
    ])
    @allure.title("Изменение раздела в справочнике Типы библиотечных экземпляров")
    @pytest.mark.regress
    def test_change_example_types(self, base_page, login_page, main_page, login_logout_page, example_types_page, example_types_type, search_value):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        example_types_page.open_example_types_page()
        example_types_page.change_example_types(search_value, example_types_type)
        message = example_types_page.get_message_box()
        assert "Запись успешно изменена" in message

    @allure.title("Удаление раздела в справочнике Типы библиотечных экземпляров")
    @pytest.mark.regress
    def test_delete_example_types(self, base_page, login_page, main_page, login_logout_page, example_types_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        example_types_page.open_example_types_page()
        example_types_page.delete_example_types()
        message = example_types_page.get_message_box()
        assert "Запись успешно удалена" in message

