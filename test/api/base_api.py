import allure
import requests


class BaseAPI:
    BASE_URL = "https://edulib-general-2.edu.bars.group"
    HEADERS = {
        "Authorization": "Bearer "
    }

    @allure.description("Пагинация")
    def get_all_pages(self, url, headers):
        results = []
        while url:
            response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()
            data = response.json()
            results.extend(data.get('results', []))
            url = data.get('next')
        return results
