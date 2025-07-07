import allure
import pytest
from playwright.sync_api import Page

from page.base_page import BasePage
from page.bookfund.bookfund_data import MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22
from page.bookfund.bookfund_page import MainPage
from page.login.login_data import ROLE_DROPDOWN_ADMIN_SYS, PERSON_DROPDOWN_SMIRNOVA
from page.login.login_page import AuthLoginPage
from page.registries.lib_registry.lib_registry_page import LibRegistryPage


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
def lib_registry_page(page: Page):
    return LibRegistryPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_SMIRNOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/regression/admin/spravochniki/test_umk_regress.py::TestUMK --browser=firefox --headless
@allure.epic("Тестирование справочника Федеральный перечень учебников")
class TestLibRegistry:

    @allure.title("Добавление издания в Библиотечный реестр")
    @pytest.mark.regress
    def test_add_lib_registry(self, base_page, login_page, main_page, login_logout_page, lib_registry_page):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_registry_page("Библиотечный реестр")
        lib_registry_page.add_lib_registry()
        message = lib_registry_page.get_message_box()
        assert "Запись успешно создана" in message
        row = lib_registry_page.get_table_row_by_values("Действующие", "Учебник, учебная литература",
                                                         "Алгебра (в 2 частях)",
                                                         "9 параллель",
                                                         "Часть 1: Мордкович А.Г., Семенов П.В.; Часть 2: Мордкович А.Г., Александрова А.Л., Мишустина Т.Н. идругие; подредакцией Мордковича А.Г.")
        assert row is not None, "❌ Строка таблицы с указанными значениями не найдена или не отображается."