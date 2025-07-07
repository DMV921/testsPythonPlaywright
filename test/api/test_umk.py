from rapidus import Client
import allure
import pytest
import requests
import json
from test.api.base_api import BaseAPI

@allure.epic("API тесты для справочника УМК")
class TestUMKAPI(BaseAPI):
    umk_id = None # атрибут класса для хранения id УМК

    # === Основные разделы ===
    @allure.title("Добавление УМК")
    @pytest.mark.api
    def test_post_umk(self):
        client = Client(base_url=f"{self.BASE_URL}/api/education_books/v1", use_session=True)
        payload = {
            "study_level_id": 1,
            "parallel_id": 8,
            "count": 2147483647,
            "status": True,
            "school_id": 1
        }

        response = client.send_request(
            method="POST",
            endpoint="/lib_umk/",
            json=payload,
            verify = False,
            headers = self.HEADERS
        )

        response.assert_status_code(201).assert_json_contains("id")
        UMK = response.json_data  # ✅ правильный способ получения JSON
        TestUMKAPI.umk_id = UMK["id"]
        client.close()

    @pytest.mark.parametrize(("level_of_education", "parallel", "number_of_umk", "set_checkbox"), [
        ("1", "5", "50", False),
        ("1", "11", "99", True),
        ("1", "2", "2", False),
        ("1", "10", "10", True),
        ("2", "5", "99", False),
        ("2", "11", "2", True),
        ("2", "2", "10", False),
        ("2", "10", "5", True),
        ("2", "1", "1", False),
        ("3", "11", "10", True),
        ("3", "2", "5", False),
        ("3", "10", "1", True),
        ("3", "1", "50", False),
        ("3", "1", "99", True),
        ("3", "5", "2", False),
        ("1", "2", "1", False),
        ("1", "10", "50", True),
        ("1", "1", "2", True),
        ("1", "5", "10", False),
        ("1", "11", "5", True),
        ("2", "10", "99", True),
        ("2", "5", "5", False),
        ("2", "11", "1", True),
        ("2", "2", "50", False),
        ("3", "1", "10", False),
        ("3", "1", "5", True),
        ("3", "5", "1", False),
        ("3", "11", "50", True),
        ("3", "2", "99", False),
        ("3", "10", "2", True),
    ])
    @allure.title("Добавление записей в справочник УМК с различными входными параметрами")
    @pytest.mark.api
    def test_post_all_params_umk(self, level_of_education, parallel, number_of_umk, set_checkbox):
        client = Client(base_url=f"{self.BASE_URL}/api/education_books/v1", use_session=True)
        payload = {
            "study_level_id": level_of_education,
            "parallel_id": parallel,
            "count": number_of_umk,
            "status": set_checkbox,
            "school_id": 1
        }

        response = client.send_request(
            method="POST",
            endpoint="/lib_umk/",
            json=payload,
            verify = False,
            headers = self.HEADERS
        )

        response.assert_status_code(201).assert_json_contains("id")
        client.send_request(
            method="DELETE",
            endpoint=f"/lib_umk/{response.json_data['id']}/",
            verify=False,
            headers=self.HEADERS

        ).assert_status_code(204).assert_response_time(1999)
        client.close()

    @allure.title("Получение УМК")
    @pytest.mark.api
    def test_get_umk(self):
        client = Client(base_url="https://edulib-general-2.edu.bars.group/api/education_books/v1", use_session=True)

        client.send_request(
            method="GET",
            endpoint=f"/lib_umk/{TestUMKAPI.umk_id}/",
            verify=False,
            headers=self.HEADERS

        ).assert_status_code(200).assert_response_time(1999).assert_json_contains("id", TestUMKAPI.umk_id)

         # ✅ правильный способ получения JSON
        client.close()

    @pytest.mark.parametrize(("level_of_education", "parallel", "number_of_umk", "set_checkbox"), [
        ("1", "5", "50", False),
        ("1", "11", "99", True),
        ("1", "2", "2", False),
        ("1", "10", "10", True),
        ("2", "5", "99", False),
        ("2", "11", "2", True),
        ("2", "2", "10", False),
        ("2", "10", "5", True),
        ("2", "1", "1", False),
        ("3", "11", "10", True),
        ("3", "2", "5", False),
        ("3", "10", "1", True),
        ("3", "1", "50", False),
        ("3", "1", "99", True),
        ("3", "5", "2", False),
        ("1", "2", "1", False),
        ("1", "10", "50", True),
        ("1", "1", "2", True),
        ("1", "5", "10", False),
        ("1", "11", "5", True),
        ("2", "10", "99", True),
        ("2", "5", "5", False),
        ("2", "11", "1", True),
        ("2", "2", "50", False),
        ("3", "1", "10", False),
        ("3", "1", "5", True),
        ("3", "5", "1", False),
        ("3", "11", "50", True),
        ("3", "2", "99", False),
        ("3", "10", "2", True),
    ])
    @allure.title("Изменение УМК")
    @pytest.mark.api
    def test_patch_umk(self, level_of_education, parallel, number_of_umk, set_checkbox):
        client = Client(base_url="https://edulib-general-2.edu.bars.group/api/education_books/v1", use_session=True)
        payload = {
            "study_level_id": level_of_education,
            "parallel_id": parallel,
            "count": number_of_umk,
            "status": set_checkbox,
            "school_id": 1
        }

        client.send_request(
            method="PATCH",
            endpoint=f"/lib_umk/{TestUMKAPI.umk_id}/",
            json=payload,
            verify=False,
            headers=self.HEADERS

        ).assert_status_code(200).assert_response_time(3600).assert_json_contains("id", TestUMKAPI.umk_id)

        # ✅ правильный способ получения JSON
        client.close()

    @allure.title("Удаление УМК")
    @pytest.mark.api
    def test_delete_umk(self):
        client = Client(base_url="https://edulib-general-2.edu.bars.group/api/education_books/v1", use_session=True)

        client.send_request(
            method="DELETE",
            endpoint=f"/lib_umk/{TestUMKAPI.umk_id}/",
            verify=False,
            headers=self.HEADERS

        ).assert_status_code(204).assert_response_time(500)

        # ✅ правильный способ получения JSON
        client.close()
