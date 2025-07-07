import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Авторы")
class TestAuthorsAPI(BaseAPI):
    author_id = None # атрибут класса для хранения id автора
    @allure.title("Добавление автора")
    @pytest.mark.api
    def test_post_author(self):
        data = {
            "name": "Тестовый автор"
        }
        response = requests.post(f"{self.BASE_URL}/api/education_books/v1/authors/", headers=self.HEADERS, json=data, verify=False)
        assert response.status_code == 201, f"Автор не создан: {response.status_code}, {response.text}"
        result = response.json()
        assert result["name"] == data["name"], "Имя автора не совпадает"
        author = response.json()
        TestAuthorsAPI.author_id = author["id"]  # сохраняем id в атрибут класса

    @allure.title("Получение автора по id и name и поиск его в общем списке")
    @pytest.mark.api
    def test_get_author(self):
        assert TestAuthorsAPI.author_id is not None, "ID автора не установлен после создания"
        single_author_responce = requests.get(
            f"{self.BASE_URL}/api/education_books/v1/authors/?limit=100&search=Тестовый автор", headers=self.HEADERS,
            verify=False)
        assert single_author_responce.status_code == 200, "Ошибка при получении данных об авторе"
        single_author_result = single_author_responce.json()['results']
        found_author = next((author for author in single_author_result
                             if author["id"] == TestAuthorsAPI.author_id and author["name"] == "Тестовый автор"), None)
        assert found_author is not None, f"Автор с id={TestAuthorsAPI.author_id} и name='Тестовый автор' не найден в результатах поиска"
        all_authors_responce = requests.get(f"{self.BASE_URL}/api/education_books/v1/authors/?limit=1000", headers=self.HEADERS,
                                            verify=False)
        assert all_authors_responce.status_code == 200, "Ошибка при получении данных о всех авторах"
        all_authors_list = all_authors_responce.json()['results']
        assert found_author in all_authors_list, f"Автор {found_author} не найден в полном списке авторов"

    @allure.title("Изменение автора")
    @pytest.mark.api
    def test_update_author(self):
        assert TestAuthorsAPI.author_id is not None, "Автор не был создан"
        data = {"name": "Тестовый автор изменение"}
        response = requests.patch(f"{self.BASE_URL}/api/education_books/v1/authors/{TestAuthorsAPI.author_id}/", headers=self.HEADERS, json=data,
                                  verify=False)
        assert response.status_code == 200
        updated_author = response.json()
        assert updated_author["name"] == "Тестовый автор изменение"

    @allure.title("Удаление автора")
    @pytest.mark.api
    def test_delete_author(self):
        assert TestAuthorsAPI.author_id is not None, "Автор не был создан"
        response = requests.delete(f"{self.BASE_URL}/api/education_books/v1/authors/{TestAuthorsAPI.author_id}/", headers=self.HEADERS,
                                  verify=False)
        assert response.status_code == 204
