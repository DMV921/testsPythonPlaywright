import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Типы библиотечных экземпляров")
class TestExampleTypesAPI(BaseAPI):
    example_type_id = None # атрибут класса для хранения id типа библиотечного экземпляра
    @allure.title("Добавление типа библиотечного экземпляра")
    @pytest.mark.api
    def test_post_example_types(self):
        data = {
            "name": "Тестовый тип библиотечного экземпляра API",
            "release_method": 1
        }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/example-types/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Тип библиотечного экземпляра не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя типа библиотечного экземпляра не совпадает"
        assert result["release_method"] == data["release_method"], "Тип библиотечного экземпляра не совпадает"
        example_type = response.json()
        TestExampleTypesAPI.example_type_id = example_type["id"] # сохраняем id в атрибут класса

    @allure.title("Добавление и удаление типов библиотечных экземпляров с типами Электронные (медиафайл и др) и Периодика")
    @pytest.mark.api
    @pytest.mark.parametrize("release_method", [2, 3])
    def test_create_and_delete_example_type_with_different_release_methods(self, release_method):
        data = {
            "name": f"Тестовый тип с release_method {release_method}",
            "release_method": release_method
        }
        # Создаем
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/example-types/", headers=self.HEADERS,
                                 json=data, verify=False)
        assert response.status_code == 201, f"Тип не создан с release_method={release_method}: {response.status_code}, {response.text}"
        result = response.json()
        assert result["release_method"] == release_method, "release_method не совпадает после создания"

        # Удаляем созданный тип
        delete_response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/example-types/{result['id']}/",
                                          headers=self.HEADERS, verify=False)
        assert delete_response.status_code == 204, f"Не удалось удалить тип с id={result['id']}"

    @allure.title("Получение типа библиотечного экземпляра по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_example_types(self):
        assert TestExampleTypesAPI.example_type_id is not None, "ID Типа библиотечного экземпляра не установлено после создания"
        single_example_type_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/example-types/?limit=100&search=Тестовый тип библиотечного экземпляра", headers=self.HEADERS,
            verify=False)
        assert single_example_type_responce.status_code == 200, "Ошибка при получении данных об источнике поступления"
        single_example_type_result = single_example_type_responce.json()['results']
        found_example_type = next((example_type for example_type in single_example_type_result
                             if example_type["id"] == TestExampleTypesAPI.example_type_id and example_type["name"] == "Тестовый тип библиотечного экземпляра API"), None)
        assert found_example_type is not None, f"Тип библиотечного экземпляра с id={TestExampleTypesAPI.example_type_id} и name='Тестовый тип библиотечного экземпляра' не найден в результатах поиска"
        all_example_types_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/example-types/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_example_types_responce.status_code == 200, "Ошибка при получении данных о всех источниках поступления"
        all_example_types_list = all_example_types_responce.json()['results']
        assert found_example_type in all_example_types_list, f"Тип библиотечного экземпляра {found_example_type} не найден в полном списке источников поступления"

    @pytest.mark.parametrize(("name","release_method"), [
        ("Тестовый тип библиотечного экземпляра API изменение", 2),
        ("Тестовый тип библиотечного экземпляра API изменение 2", 3),
        ("Тестовый тип библиотечного экземпляра API изменение 3", 1)
    ])
    @allure.title("Изменение типа библиотечного экземпляра")
    @pytest.mark.api
    def test_update_example_type(self, name, release_method):
        assert TestExampleTypesAPI.example_type_id is not None, "Тип библиотечного экземпляра не был создан"
        data = {
            "name": name,
            "release_method": release_method
        }
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/example-types/{TestExampleTypesAPI.example_type_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_example_types = response.json()
        assert updated_example_types["name"] == name
        assert updated_example_types["release_method"] == release_method

    @allure.title("Удаление типа библиотечного экземпляра")
    @pytest.mark.api
    def test_delete_example_type(self):
        assert TestExampleTypesAPI.example_type_id is not None, "Тип библиотечного экземпляра не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/example-types/{TestExampleTypesAPI.example_type_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204
