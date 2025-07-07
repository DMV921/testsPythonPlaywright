import allure
import pytest
from playwright.sync_api import Page
from page.admin.umk.umk_page import UMKPage
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
def umk_page(page: Page):
    return UMKPage(page)

@pytest.fixture
def login_logout_page(page: Page, login_page, main_page, request):
    role = getattr(request, "param", ROLE_DROPDOWN_ADMIN_SYS)
    person = getattr(request, "param", PERSON_DROPDOWN_KUZNECOVA)
    login_page.auth(role, person)
    yield login_page.page
    main_page.logout()

# pytest test/regression/admin/spravochniki/test_umk_regress.py::TestUMK --browser=firefox --headless
@allure.epic("Тестирование справочника УМК")
class TestUMK:

    @pytest.mark.parametrize(("level_of_education", "parallel", "number_of_umk", "set_checkbox"), [
        ("Начальное общее образование", "9 параллель", "1", False),
    ])
    @allure.title("Добавление раздела в справочник УМК")
    @pytest.mark.regress
    def test_add_umk(self, base_page, login_page, main_page, login_logout_page, umk_page, level_of_education, parallel, number_of_umk, set_checkbox):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        umk_page.open_umk_page()
        umk_page.add_umk(level_of_education, parallel, number_of_umk, set_checkbox)
        message = umk_page.get_message_box()
        assert "Запись успешно создана" in message
        
    @pytest.mark.parametrize(("level_of_education", "parallel", "number_of_umk", "set_checkbox"), [
        ("Начальное общее образование", "5 параллель", "50", False),
        ("Начальное общее образование", "11 параллель", "99", True),
        ("Начальное общее образование", "2 параллель", "2", False),
        ("Начальное общее образование", "10 параллель", "10", True),
        ("Основное общее образование", "5 параллель", "99", False),
        ("Основное общее образование", "11 параллель", "2", True),
        ("Основное общее образование", "2 параллель", "10", False),
        ("Основное общее образование", "10 параллель", "5", True),
        ("Основное общее образование", "1 параллель", "1", False),
        ("Среднее общее образование", "11 параллель", "10", True),
        ("Среднее общее образование", "2 параллель", "5", False),
        ("Среднее общее образование", "10 параллель", "1", True),
        ("Среднее общее образование", "1 параллель", "50", False),
        ("Среднее общее образование", "1 параллель", "99", True),
        ("Среднее общее образование", "5 параллель", "2", False),
        ("Начальное общее образование", "2 параллель", "1", False),
        ("Начальное общее образование", "10 параллель", "50", True),
        ("Начальное общее образование", "1 параллель", "2", True),
        ("Начальное общее образование", "5 параллель", "10", False),
        ("Начальное общее образование", "11 параллель", "5", True),
        ("Основное общее образование", "10 параллель", "99", True),
        ("Основное общее образование", "5 параллель", "5", False),
        ("Основное общее образование", "11 параллель", "1", True),
        ("Основное общее образование", "2 параллель", "50", False),
        ("Среднее общее образование", "1 параллель", "10", False),
        ("Среднее общее образование", "1 параллель", "5", True),
        ("Среднее общее образование", "5 параллель", "1", False),
        ("Среднее общее образование", "11 параллель", "50", True),
        ("Среднее общее образование", "2 параллель", "99", False),
        ("Среднее общее образование", "10 параллель", "2", True),
    ])
    @allure.title("Добавление разделов в справочник УМК с различными входными параметрами")
    @pytest.mark.regress
    def test_add_all_params_umk(self, base_page, login_page, main_page, login_logout_page, umk_page, level_of_education, parallel, number_of_umk, set_checkbox):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        umk_page.open_umk_page()
        umk_page.add_umk(level_of_education, parallel, number_of_umk, set_checkbox)
        message = umk_page.get_message_box()
        assert "Запись успешно создана" in message
        umk_page.delete_umk(parallel)
        message = umk_page.wait_for_message("Запись успешно удалена")
        assert "Запись успешно удалена" in message

    @pytest.mark.parametrize(("level_of_education","parallel", "number_of_umk", "set_checkbox", "parallel_for_changing"), [
        ("Основное общее образование","5 параллель", "5", False, "9 параллель"),
        ("Начальное общее образование", "5 параллель", "50", False, "5 параллель"),
        ("Начальное общее образование", "11 параллель", "99", True, "5 параллель"),
        ("Начальное общее образование", "2 параллель", "2", False, "11 параллель"),
        ("Начальное общее образование", "10 параллель", "10", True, "2 параллель"),
        ("Основное общее образование", "5 параллель", "99", False, "10 параллель"),
        ("Основное общее образование", "11 параллель", "2", True, "5 параллель"),
        ("Основное общее образование", "2 параллель", "10", False, "11 параллель"),
        ("Основное общее образование", "10 параллель", "5", True, "2 параллель"),
        ("Основное общее образование", "1 параллель", "1", False, "10 параллель"),
        ("Среднее общее образование", "11 параллель", "10", True, "1 параллель"),
        ("Среднее общее образование", "2 параллель", "5", False, "11 параллель"),
        ("Среднее общее образование", "10 параллель", "1", True, "2 параллель"),
        ("Среднее общее образование", "1 параллель", "50", False, "10 параллель"),
        ("Среднее общее образование", "1 параллель", "99", True, "1 параллель"),
        ("Среднее общее образование", "5 параллель", "2", False, "1 параллель"),
        ("Начальное общее образование", "2 параллель", "1", False, "5 параллель"),
        ("Начальное общее образование", "10 параллель", "50", True, "2 параллель"),
        ("Начальное общее образование", "1 параллель", "2", True, "10 параллель"),
        ("Начальное общее образование", "5 параллель", "10", False, "1 параллель"),
        ("Начальное общее образование", "11 параллель", "5", True, "5 параллель"),
        ("Основное общее образование", "10 параллель", "99", True, "11 параллель"),
        ("Основное общее образование", "5 параллель", "5", False, "10 параллель"),
        ("Основное общее образование", "11 параллель", "1", True, "5 параллель"),
        ("Основное общее образование", "2 параллель", "50", False, "11 параллель"),
        ("Среднее общее образование", "1 параллель", "10", False, "2 параллель"),
        ("Среднее общее образование", "1 параллель", "5", True, "1 параллель"),
        ("Среднее общее образование", "5 параллель", "1", False, "1 параллель"),
        ("Среднее общее образование", "11 параллель", "50", True, "5 параллель"),
        ("Среднее общее образование", "2 параллель", "99", False, "11 параллель"),
        ("Среднее общее образование", "10 параллель", "2", True, "2 параллель"),
    ])
    @allure.title("Изменение раздела в справочнике УМК")
    @pytest.mark.regress
    def test_change_umk(self, base_page, login_page, main_page, login_logout_page, umk_page, level_of_education, parallel, number_of_umk, set_checkbox, parallel_for_changing):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        umk_page.open_umk_page()
        umk_page.change_umk(level_of_education, parallel, number_of_umk, set_checkbox, parallel_for_changing)
        message = umk_page.get_message_box()
        assert "Запись успешно изменена" in message

    @pytest.mark.parametrize("level_of_education, parallel, number_of_umk, set_checkbox", [
        ("Среднее общее образование", "10 параллель", "2", "Да")
    ])
    @allure.title("Удаление раздела в справочнике УМК")
    @pytest.mark.regress
    def test_delete_umk(self, base_page, login_page, main_page, login_logout_page, umk_page, level_of_education, parallel, number_of_umk, set_checkbox):
        main_page.select_schooldropdown_main_page(MAIN_PAGE_SCHOOL_SELECTOR_MBOY_SOSH_22)
        main_page.open_admin_page()
        umk_page.open_umk_page()
        umk_page.delete_umk(level_of_education, parallel, number_of_umk, set_checkbox)
        message = umk_page.get_message_box()
        assert "Запись успешно удалена" in message

