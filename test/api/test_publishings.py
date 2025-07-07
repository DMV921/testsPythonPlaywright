import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Издательства")
class TestPublishingsAPI(BaseAPI):
    publishing_id = None # атрибут класса для хранения id издательства
    @allure.title("Добавление издательства")
    @pytest.mark.api
    def test_post_publishing(self):
        data = {
            "name": "Тестовое издательство"
        }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/publishings/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Издательство не создано: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя издательства не совпадает"
        publishing = response.json()
        TestPublishingsAPI.publishing_id = publishing["id"] # сохраняем id в атрибут класса

    @allure.title("Получение издательства по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_publishing(self):
        assert TestPublishingsAPI.publishing_id is not None, "ID издательства не установлено после создания"
        single_publishing_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/publishings/?limit=100&search=Тестовое издательство", headers=self.HEADERS,
            verify=False)
        assert single_publishing_responce.status_code == 200, "Ошибка при получении данных об авторе"
        single_publishing_result = single_publishing_responce.json()['results']
        found_publishing = next((publishing for publishing in single_publishing_result
                             if publishing["id"] == TestPublishingsAPI.publishing_id and publishing["name"] == "Тестовое издательство"), None)
        assert found_publishing is not None, f"Издательство с id={TestPublishingsAPI.publishing_id} и name='Тестовое издательство' не найден в результатах поиска"
        all_publishings_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/publishings/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_publishings_responce.status_code == 200, "Ошибка при получении данных о всех издательствах"
        all_publishings_list = all_publishings_responce.json()['results']
        assert found_publishing in all_publishings_list, f"Издательство {found_publishing} не найдено в полном списке авторов"

    @allure.title("Изменение издательства")
    @pytest.mark.api
    def test_update_publishing(self):
        assert TestPublishingsAPI.publishing_id is not None, "Издательство не было создано"
        data = {"name": "Тестовое издательство изменение"}
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/publishings/{TestPublishingsAPI.publishing_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_publishing = response.json()
        assert updated_publishing["name"] == "Тестовое издательство изменение"

    @allure.title("Удаление издательства")
    @pytest.mark.api
    def test_delete_publishing(self):
        assert TestPublishingsAPI.publishing_id is not None, "Издательство не было создано"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/publishings/{TestPublishingsAPI.publishing_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204
