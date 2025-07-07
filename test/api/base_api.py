import allure
import requests


class BaseAPI:
    BASE_URL = "https://edulib-general-2.edu.bars.group"
    HEADERS = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTM3NzAiLCJhdWQiOiI2MToxNiIsImF0aCI6InN1ZGlyIiwic3RmIjoiMzg1MDI5IiwiaXNzIjoiaHR0cHM6Ly9lZHVsaWItZ2VuZXJhbC0yLmVkdS5iYXJzLmdyb3VwL21vY2stYXV0aC8iLCJybHMiOiJ7MTY6WzI0NTo2MTpbMV1dfSIsInJnbiI6IjE2IiwiaWF0IjoxNzUxMDEyNDAyLCJqdGkiOiIxYmMwZGJjZC05YTg0LTRkODQtYjU0Zi01OTUxZjhhZTg4MmIiLCJleHAiOjE3NTE4NzY0MDIsIm5iZiI6MTc1MTAxMjQwMn0.L71zQiNRiMePUtaP1Zu8IcJ1ak2Mw0ljaEb1NoqGMyO6sPquAq08RUPSqphNbPtUCtlwsNegBImwAMYlnRg8IKXK1bVTwkAGDFFnngC8V4AFJ4iwSKJtP_JfcXgo_M5c1khsKTdkv772KjRCUAnQ5hrrTKmb0EBA3nkiOxLg5CG8JNPa90Hp8HQtW9lmiCh6lgY1KqyWcB9lZRYOxR_rt1VxWxnr6EHnIauh71nUvafrqqOoHnS9msqH7FPZpLe_fRM6PRdw5goz4k22Yz_bPMXKd5SooKlhlNvrKMu_3tdva6mDnohCey8oNThF7ntgS9HsC0gM3PzCOyeG6dtV7g"
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