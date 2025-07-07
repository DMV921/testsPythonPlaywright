import os
import allure
import pytest
import requests
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника Федеральный перечень учебников")
class TestFederalBooksAPI(BaseAPI):
    @allure.title("Импорт файла в Федеральный перечень учебников")
    @pytest.mark.api
    def test_post_import_federal_books(self):
        relative_path = "page/admin/federal_books/files/Федеральный перечень для загрузки.xlsx"
        # Получаем корень проекта (например, если файл лежит в test/api/, отступаем на 2 уровня вверх)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        # Собираем абсолютный путь
        file_path = os.path.normpath(os.path.join(project_root, *relative_path.split('/')))

        with open(file_path, "rb") as f:
            files = {"file": ("Федеральный перечень для загрузки.xlsx", f,
                              "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
            response = requests.post(f"{self.BASE_URL}/api/education_books/v1/fed_books/import/", headers=self.HEADERS,
                                     files=files, verify=False)
        assert response.status_code == 202, f"Файл не импортирован: {response.status_code}, {response.text}"
        print(response.status_code)
        print(response.text)

    @allure.title("Проверка создания записи в справочнике Федеральный перечень учебников")
    @pytest.mark.api
    def test_get_import_federal_books(self):
        # Ожидаемые данные
        expected_item = {
            "name": "Тестовая новая",
            "author": {
                "name": "Виноградов Ю.М., Федорова А.Р."
            },
            "publishing": {
                "name": "Акционерное общество «Издательство «Просвещение»"
            },
            "pub_lang": "русский язык",
            "status": True,
            "code": "1.1.1.2.1.3.61",
           # "parallel":[9, 11],
            "validity_period": "2027-04-25"
        }

        all_items = self.get_all_pages(f"{self.BASE_URL}/api/education_books/v1/fed_books/", self.HEADERS)

        found = False
        for item in all_items:
            if (
                    item["name"] == expected_item["name"]
                    and item["author"]["name"] == expected_item["author"]["name"]
                    and item["publishing"]["name"] == expected_item["publishing"]["name"]
                    and item["pub_lang"] == expected_item["pub_lang"]
                    and item["status"] == expected_item["status"]
                    and item["code"] == expected_item["code"]
                    and item["validity_period"] == expected_item["validity_period"]
                  #  and item["parallel"] == expected_item["parallel"]
            ):
                print("✅ Найдена точная запись:", item)
                found = True
                break

        assert found, f"❌ Запись с такими атрибутами не найдена в ответе: {all_items}"
