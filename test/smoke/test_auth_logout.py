import allure
import pytest
from playwright.sync_api import Page

from page.admin.audit_log.audit_log_data import AUDIT_LOG_PAGE_URL
from page.admin.authors.authors_data import AUTHORS_PAGE_URL
from page.admin.bbk.bbk_data import BBK_PAGE_URL
from page.admin.classes.classes_data import CLASSES_PAGE_URL
from page.admin.disciplines.disciplines_data import DISCIPLINES_PAGE_URL
from page.admin.employees.employees_data import EMPLOYEES_PAGE_URL
from page.admin.example_types.example_types_data import EXAMPLE_TYPES_PAGE_URL
from page.admin.federal_books.federal_books_data import FEDERAL_BOOKS_PAGE_URL
from page.admin.marks.marks_data import MARKS_PAGE_URL
from page.admin.publishings.publishings_data import PUBLISHINGS_PAGE_URL
from page.admin.roles.roles_data import ROLES_PAGE_URL
from page.admin.schoolchildren.schoolchildren_data import SCHOOLCHILDREN_PAGE_URL
from page.admin.schools.schools_data import SCHOOLS_PAGE_URL
from page.admin.sources.sources_data import SOURCES_PAGE_URL
from page.admin.study_periods.study_periods_data import STUDY_PERIODS_PAGE_URL
from page.admin.udc.udc_data import UDC_PAGE_URL
from page.admin.umk.umk_data import UMK_PAGE_URL
from page.bookfund.async_tasks.async_tasks_data import ASYNC_TASKS_PAGE_URL
from page.bookfund.bookfund_data import MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22
from page.bookfund.lib_passport.lib_passport_data import LIB_PASSPORT_PAGE_URL
from page.login.login_data import ROLE_DROPDOWN_ADMIN_SYS, ROLE_DROPDOWN_ADMIN_FONDA_OO
from page.login.login_page import AuthLoginPage
from page.bookfund.bookfund_page import MainPage
from page.base_page import BASE_URL, BasePage
from page.registries.events.events_data import EVENTS_PAGE_URL
from page.registries.exchange_fund.exchange_fund_data import EXCHANGE_FUND_PAGE_URL
from page.registries.general_fund.general_fund_data import GENERAL_FUND_PAGE_URL
from page.registries.issuances.issuances_data import ISSUANCES_PAGE_URL
from page.registries.lib_registry.lib_registry_data import LIB_REGISTRY_PAGE_URL
from page.registries.library_catalog.library_catalog_data import LIBRARY_CATALOG_PAGE_URL
from page.registries.reader_requests.reader_requests_data import READER_REQUEST_PAGE_URL
from page.registries.readers.readers_data import READERS_PAGE_URL
from page.registries.readers_books.readers_books_data import READERS_BOOKS_PAGE_URL
from page.registries.readers_requests.readers_requests_data import READERS_REQUESTS_PAGE_URL


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
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    login_page.auth(role)
    yield login_page.page
    main_page.logout()


# pytest test/smoke/test_auth_logout.py::TestSmoke --browser=firefox --headless
@allure.epic("Дымы")
class TestSmoke:

    @allure.title("Переход на страницу справочника Авторы")
    @pytest.mark.smoke
    def test_authors_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(AUTHORS_PAGE_URL)
        base_page.actions.wait(2)
        base_page.asserts.url_is(AUTHORS_PAGE_URL)

    @allure.title("Переход на страницу справочника Знак информационной продукции")
    @pytest.mark.smoke
    def test_marks_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(MARKS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(MARKS_PAGE_URL)

    @allure.title("Переход на страницу справочника Издательства")
    @pytest.mark.smoke
    def test_publishings_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(PUBLISHINGS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(PUBLISHINGS_PAGE_URL)

    @allure.title("Переход на страницу справочника Источники поступления")
    @pytest.mark.smoke
    def test_sources_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(SOURCES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(SOURCES_PAGE_URL)

    @allure.title("Переход на страницу справочника Классы")
    @pytest.mark.smoke
    def test_classes_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(CLASSES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(CLASSES_PAGE_URL)

    @allure.title("Переход на страницу справочника Организации")
    @pytest.mark.smoke
    def test_schools_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(SCHOOLS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(SCHOOLS_PAGE_URL)

    @allure.title("Переход на страницу справочника Периоды обучения")
    @pytest.mark.smoke
    def test_study_periods_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(STUDY_PERIODS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(STUDY_PERIODS_PAGE_URL)

    @allure.title("Переход на страницу справочника Предметы")
    @pytest.mark.smoke
    def test_disciplines_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(DISCIPLINES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(DISCIPLINES_PAGE_URL)

    @allure.title("Переход на страницу справочника Разделы ББК")
    @pytest.mark.smoke
    def test_bbk_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(BBK_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(BBK_PAGE_URL)

    @allure.title("Переход на страницу справочника Разделы УДК")
    @pytest.mark.smoke
    def test_udc_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(UDC_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(UDC_PAGE_URL)

    @allure.title("Переход на страницу справочника Сотрудники")
    @pytest.mark.smoke
    def test_employees_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(EMPLOYEES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(EMPLOYEES_PAGE_URL)

    @allure.title("Переход на страницу справочника Типы библиотечных экземпляров")
    @pytest.mark.smoke
    def test_example_types_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(EXAMPLE_TYPES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(EXAMPLE_TYPES_PAGE_URL)

    @allure.title("Переход на страницу справочника Ученики")
    @pytest.mark.smoke
    def test_schoolchildren_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(SCHOOLCHILDREN_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(SCHOOLCHILDREN_PAGE_URL)

    @allure.title("Переход на страницу справочника УМК")
    @pytest.mark.smoke
    def test_umk_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(UMK_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(UMK_PAGE_URL)

    @allure.title("Переход на страницу справочника Федеральный перечень учебников")
    @pytest.mark.smoke
    def test_federal_books_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(FEDERAL_BOOKS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(FEDERAL_BOOKS_PAGE_URL)

    @allure.title("Переход на страницу Роли и права")
    @pytest.mark.smoke
    def test_roles_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(ROLES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(ROLES_PAGE_URL)

    @allure.title("Переход на страницу Журнал изменений")
    @pytest.mark.smoke
    def test_audit_log_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(AUDIT_LOG_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(AUDIT_LOG_PAGE_URL)

    #Реестры
    @allure.title("Переход на страницу Библиотечного реестра")
    @pytest.mark.smoke
    def test_lib_registry_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(LIB_REGISTRY_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(LIB_REGISTRY_PAGE_URL)

    @allure.title("Переход на страницу реестра Выдача/сдача экземпляров")
    @pytest.mark.smoke
    def test_issuances_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(ISSUANCES_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(ISSUANCES_PAGE_URL)

    @allure.title("Переход на страницу реестра Желаемая литература")
    @pytest.mark.smoke
    def test_readers_requests_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(READERS_REQUESTS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(READERS_REQUESTS_PAGE_URL)

    @allure.title("Переход на страницу реестра Каталог изданий")
    @pytest.mark.smoke
    def test_library_catalog_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(LIBRARY_CATALOG_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(LIBRARY_CATALOG_PAGE_URL)

    @allure.title("Переход на страницу реестра Книгообменный фонд")
    @pytest.mark.smoke
    @pytest.mark.parametrize("login_logout_page", [ROLE_DROPDOWN_ADMIN_FONDA_OO], indirect=True)
    def test_exchange_fund_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(EXCHANGE_FUND_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(EXCHANGE_FUND_PAGE_URL)

    @allure.title("Переход на страницу реестра Мои заявки на заказ изданий")
    @pytest.mark.smoke
    def test_reader_requests_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(READER_REQUEST_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(READER_REQUEST_PAGE_URL)

    @allure.title("Переход на страницу реестра Моя литература")
    @pytest.mark.smoke
    def test_readers_books_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(READERS_BOOKS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(READERS_BOOKS_PAGE_URL)

    @allure.title("Переход на страницу реестра Общий фонд литературы")
    @pytest.mark.smoke
    def test_general_fund_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(GENERAL_FUND_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(GENERAL_FUND_PAGE_URL)

    @allure.title("Переход на страницу Реестр библиотечных мероприятий")
    @pytest.mark.smoke
    def test_events_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(EVENTS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(EVENTS_PAGE_URL)

    @allure.title("Переход на страницу Реестр читателей")
    @pytest.mark.smoke
    def test_readers_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(READERS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(READERS_PAGE_URL)

    @allure.title("Переход на страницу Асинхронные задачи")
    @pytest.mark.smoke
    def test_async_tasks_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(ASYNC_TASKS_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(ASYNC_TASKS_PAGE_URL)

    @allure.title("Переход на страницу Паспорт библиотеки")
    @pytest.mark.smoke
    def test_lib_passport_page(self, base_page, login_page, main_page, login_logout_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        base_page.actions.navigate(LIB_PASSPORT_PAGE_URL)
        base_page.actions.wait(5)
        base_page.asserts.url_is(LIB_PASSPORT_PAGE_URL)
