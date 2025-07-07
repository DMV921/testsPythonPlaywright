import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Источники поступления")
class TestSourcesAPI(BaseAPI):
    source_id = None # атрибут класса для хранения id источника поступления
    @allure.title("Добавление источника поступления")
    @pytest.mark.api
    def test_post_sources(self):
        data = {
            "name": "Тестовый источник поступления"
        }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/sources/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Источник поступления не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя источника поступления не совпадает"
        source = response.json()
        TestSourcesAPI.source_id = source["id"] # сохраняем id в атрибут класса

    @allure.title("Получение источника поступления по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_sources(self):
        assert TestSourcesAPI.source_id is not None, "ID Источника поступления не установлено после создания"
        single_source_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/sources/?limit=100&search=Тестовый источник поступления", headers=self.HEADERS,
            verify=False)
        assert single_source_responce.status_code == 200, "Ошибка при получении данных об источнике поступления"
        single_source_result = single_source_responce.json()['results']
        found_source = next((source for source in single_source_result
                             if source["id"] == TestSourcesAPI.source_id and source["name"] == "Тестовый источник поступления"), None)
        assert found_source is not None, f"Источник поступления с id={TestSourcesAPI.source_id} и name='Тестовый источник поступления' не найден в результатах поиска"
        all_sources_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/sources/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_sources_responce.status_code == 200, "Ошибка при получении данных о всех источниках поступления"
        all_sources_list = all_sources_responce.json()['results']
        assert found_source in all_sources_list, f"Источник поступления {found_source} не найден в полном списке источников поступления"

    @allure.title("Изменение источника поступления")
    @pytest.mark.api
    def test_update_source(self):
        assert TestSourcesAPI.source_id is not None, "Источник постуления не был создан"
        data = {"name": "Тестовый источник поступления изменение"}
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/sources/{TestSourcesAPI.source_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_sources = response.json()
        assert updated_sources["name"] == "Тестовый источник поступления изменение"

    @allure.title("Удаление источника поступления")
    @pytest.mark.api
    def test_delete_source(self):
        assert TestSourcesAPI.source_id is not None, "Источник поступления не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/sources/{TestSourcesAPI.source_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204
