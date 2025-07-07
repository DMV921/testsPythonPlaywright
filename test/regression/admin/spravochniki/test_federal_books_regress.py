import allure
import pytest
from playwright.sync_api import Page
from page.admin.federal_books.federal_books_page import FederalBooksPage
from page.base_page import BasePage
from page.bookfund.bookfund_data import MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22
from page.bookfund.bookfund_page import MainPage
from page.login.login_data import ROLE_DROPDOWN_ADMIN_SYS, PERSON_DROPDOWN_KUZNECOVA, PERSON_DROPDOWN_SMIRNOVA
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
def federal_books_page(page: Page):
    return FederalBooksPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/regression/admin/spravochniki/test_umk_regress.py::TestUMK --browser=firefox --headless
@allure.epic("Тестирование справочника Федеральный перечень учебников")
class TestFederalBooks:

    @allure.title("Импорт в справочник Федеральный перечень учебников")
    @pytest.mark.regress
    def test_import_federal_books(self, base_page, login_page, main_page, login_logout_page, federal_books_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        federal_books_page.open_federal_books_page()
        federal_books_page.import_federal_books()
        message = federal_books_page.get_message_box()
        assert 'Задача поставлена в очередь. Результат можно посмотреть в реестре "Асинхронные задачи"' in message
        federal_books_page.select_from_dropdown_sort("По актуальности (А-Я)")
        row = federal_books_page.get_table_row_by_values( "1.1.1.2.1.3.61", "Тестовая новая", "Виноградов Ю.М., Федорова А.Р.", "Акционерное общество «Издательство «Просвещение»", "русский язык", "25.04.2027", "Да")
        assert row is not None, "❌ Строка таблицы с указанными значениями не найдена или не отображается."