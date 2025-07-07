import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Разделы ББК")
class TestBBKAPI(BaseAPI):
    bbk_id = None # атрибут класса для хранения id раздела ББК

    # === Основные разделы ===
    @allure.title("Добавление раздела ББК")
    @pytest.mark.api
    def test_post_bbk(self):
        data = {
                "code": "99999991",
                "name": "Тестовый ББК API",
                }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/bbk/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Раздел ББК не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя Раздела ББК не совпадает"
        BBK = response.json()
        TestBBKAPI.bbk_id = BBK["id"]  # сохраняем id в атрибут класса

    @allure.title("Получение раздела ББК по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_BBK(self):
        assert TestBBKAPI.bbk_id is not None, "ID раздела ББК не установлен после создания"
        single_bbk_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/bbk/?limit=100&search=Тестовый ББК", headers=self.HEADERS,
            verify=False)
        assert single_bbk_responce.status_code == 200, "Ошибка при получении данных о разделе ББК"
        single_bbk_result = single_bbk_responce.json()['results']
        found_bbk = next((bbk for bbk in single_bbk_result
                             if bbk["id"] == TestBBKAPI.bbk_id and bbk["name"] == "Тестовый ББК API"), None)
        assert found_bbk is not None, f"Раздел ББК с id={TestBBKAPI.bbk_id} и name='Тестовый ББК API' не найден в результатах поиска"
        all_bbk_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/bbk/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_bbk_responce.status_code == 200, "Ошибка при получении данных о всех разделах ББК"
        all_bbk_list = all_bbk_responce.json()['results']
        assert found_bbk in all_bbk_list, f"Раздел ББК {found_bbk} не найден в полном списке разделов ББК"

    @allure.title("Изменение раздела ББК")
    @pytest.mark.api
    def test_update_bbk(self):
        assert TestBBKAPI.bbk_id is not None, "Раздел ББК не был создан"
        data = {
                "code": "99999998",
                "name": "Тестовый ББК API Изменение",
                }
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/bbk/{TestBBKAPI.bbk_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_bbk = response.json()
        assert updated_bbk["code"] == "99999998"
        assert updated_bbk["name"] == "Тестовый ББК API Изменение"

    # === Дочерние разделы ===
    bbk_child_id = None  # атрибут класса для хранения id дочернего раздела ББК
    @allure.title("Добавление дочернего раздела ББК")
    @pytest.mark.api
    def test_post_child_bbk(self):
        data = {
                "code": "9999999999998",
                "name": "Тестовый дочерний ББК API",
                "parent_id": TestBBKAPI.bbk_id
                }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/bbk/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Дочерний раздел ББК не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя дочернего раздела ББК не совпадает"
        BBK = response.json()
        TestBBKAPI.bbk_child_id = BBK["id"]  # сохраняем id в атрибут класса

    @allure.title("Получение дочернего раздела ББК по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_child_bbk(self):
        assert TestBBKAPI.bbk_child_id is not None, "ID дочернего раздела ББК не установлен после создания"
        params = {
            "limit": 100,
            "search": "Тестовый дочерний ББК API",
            "parent_id": TestBBKAPI.bbk_id
        }
        single_child_bbk_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/bbk/", headers=self.HEADERS, params=params,
            verify=False)
        assert single_child_bbk_responce.status_code == 200, "Ошибка при получении данных о дочернем разделе ББК"
        single_child_bbk_result = single_child_bbk_responce.json()['results']
        found_child_bbk = next((child_bbk for child_bbk in single_child_bbk_result
                             if child_bbk["id"] == TestBBKAPI.bbk_child_id and child_bbk["name"] == "Тестовый дочерний ББК API"), None)
        assert found_child_bbk is not None, f"Дочерний раздел ББК с id={TestBBKAPI.bbk_child_id} и name='Тестовый дочерний ББК API' не найден в результатах поиска"
        all_child_bbk_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/bbk/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_child_bbk_responce.status_code == 200, "Ошибка при получении данных о всех разделах ББК"
        all_child_bbk_list = all_child_bbk_responce.json()['results']
        assert found_child_bbk in all_child_bbk_list, f"Дочерний раздел ББК {found_child_bbk} не найден в полном списке разделов ББК"

    @allure.title("Изменение дочернего раздела ББК")
    @pytest.mark.api
    def test_update_child_bbk(self):
        assert TestBBKAPI.bbk_child_id is not None, "Дочерний раздел ББК не был создан"
        data = {
                "code": "9999999999898",
                "name": "Тестовый дочерний ББК API Изменение",
                }
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/bbk/{TestBBKAPI.bbk_child_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_child_bbk = response.json()
        assert updated_child_bbk["code"] == "9999999999898"
        assert updated_child_bbk["name"] == "Тестовый дочерний ББК API Изменение"

    @allure.title("Удаление дочернего раздела ББК")
    @pytest.mark.api
    def test_delete_child_bbk(self):
        assert TestBBKAPI.bbk_child_id is not None, "Дочерний раздел ББК не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/bbk/{TestBBKAPI.bbk_child_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204

    # === Основные разделы ===
    @allure.title("Удаление раздела ББК")
    @pytest.mark.api
    def test_delete_bbk(self):
        assert TestBBKAPI.bbk_id is not None, "Раздел ББК не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/bbk/{TestBBKAPI.bbk_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204
