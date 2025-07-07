import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Разделы УДК")
class TestUDCAPI(BaseAPI):
    udc_id = None # атрибут класса для хранения id раздела УДК

    # === Основные разделы ===
    @allure.title("Добавление раздела УДК")
    @pytest.mark.api
    def test_post_udc(self):
        data = {
                "code": "99999991",
                "name": "Тестовый УДК API",
                }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/udc/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Раздел УДК не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя Раздела УДК не совпадает"
        UDC = response.json()
        TestUDCAPI.udc_id = UDC["id"]  # сохраняем id в атрибут класса

    @allure.title("Получение раздела УДК по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_UDC(self):
        assert TestUDCAPI.udc_id is not None, "ID раздела УДК не установлен после создания"
        single_udc_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/udc/?limit=100&search=Тестовый УДК", headers=self.HEADERS,
            verify=False)
        assert single_udc_responce.status_code == 200, "Ошибка при получении данных о разделе УДК"
        single_udc_result = single_udc_responce.json()['results']
        found_udc = next((udc for udc in single_udc_result
                             if udc["id"] == TestUDCAPI.udc_id and udc["name"] == "Тестовый УДК API"), None)
        assert found_udc is not None, f"Раздел УДК с id={TestUDCAPI.udc_id} и name='Тестовый УДК API' не найден в результатах поиска"
        all_udc_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/udc/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_udc_responce.status_code == 200, "Ошибка при получении данных о всех разделах УДК"
        all_udc_list = all_udc_responce.json()['results']
        assert found_udc in all_udc_list, f"Раздел УДК {found_udc} не найден в полном списке разделов УДК"

    @allure.title("Изменение раздела УДК")
    @pytest.mark.api
    def test_update_udc(self):
        assert TestUDCAPI.udc_id is not None, "Раздел УДК не был создан"
        data = {
                "code": "99999998",
                "name": "Тестовый УДК API Изменение",
                }
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/udc/{TestUDCAPI.udc_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_udc = response.json()
        assert updated_udc["code"] == "99999998"
        assert updated_udc["name"] == "Тестовый УДК API Изменение"

    # === Дочерние разделы ===
    udc_child_id = None  # атрибут класса для хранения id дочернего раздела УДК
    @allure.title("Добавление дочернего раздела УДК")
    @pytest.mark.api
    def test_post_child_udc(self):
        data = {
                "code": "9999999999998",
                "name": "Тестовый дочерний УДК API",
                "parent_id": TestUDCAPI.udc_id
                }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/udc/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Дочерний раздел УДК не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя дочернего раздела УДК не совпадает"
        UDC = response.json()
        TestUDCAPI.udc_child_id = UDC["id"]  # сохраняем id в атрибут класса

    @allure.title("Получение дочернего раздела УДК по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_child_udc(self):
        assert TestUDCAPI.udc_child_id is not None, "ID дочернего раздела УДК не установлен после создания"
        params = {
            "limit": 100,
            "search": "Тестовый дочерний УДК API",
            "parent_id": TestUDCAPI.udc_id
        }
        single_child_udc_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/udc/", headers=self.HEADERS, params=params,
            verify=False)
        assert single_child_udc_responce.status_code == 200, "Ошибка при получении данных о дочернем разделе УДК"
        single_child_udc_result = single_child_udc_responce.json()['results']
        found_child_udc = next((child_udc for child_udc in single_child_udc_result
                             if child_udc["id"] == TestUDCAPI.udc_child_id and child_udc["name"] == "Тестовый дочерний УДК API"), None)
        assert found_child_udc is not None, f"Дочерний раздел УДК с id={TestUDCAPI.udc_child_id} и name='Тестовый дочерний УДК API' не найден в результатах поиска"
        all_child_udc_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/udc/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_child_udc_responce.status_code == 200, "Ошибка при получении данных о всех разделах УДК"
        all_child_udc_list = all_child_udc_responce.json()['results']
        assert found_child_udc in all_child_udc_list, f"Дочерний раздел УДК {found_child_udc} не найден в полном списке разделов УДК"

    @allure.title("Изменение дочернего раздела УДК")
    @pytest.mark.api
    def test_update_child_udc(self):
        assert TestUDCAPI.udc_child_id is not None, "Дочерний раздел УДК не был создан"
        data = {
                "code": "9999999999898",
                "name": "Тестовый дочерний УДК API Изменение",
                }
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/udc/{TestUDCAPI.udc_child_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_child_udc = response.json()
        assert updated_child_udc["code"] == "9999999999898"
        assert updated_child_udc["name"] == "Тестовый дочерний УДК API Изменение"

    @allure.title("Удаление дочернего раздела УДК")
    @pytest.mark.api
    def test_delete_child_udc(self):
        assert TestUDCAPI.udc_child_id is not None, "Дочерний раздел УДК не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/udc/{TestUDCAPI.udc_child_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204

    # === Основные разделы ===
    @allure.title("Удаление раздела УДК")
    @pytest.mark.api
    def test_delete_udc(self):
        assert TestUDCAPI.udc_id is not None, "Раздел УДК не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/udc/{TestUDCAPI.udc_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204
