import json


class Checking:
    """Класс проверки ответов на http-запросы"""

    @staticmethod
    def check_status_code(response, expected_status_code: int):
        """Метод проверки статус кода ответов"""

        assert expected_status_code == response.status_code

        if expected_status_code == response.status_code:
            print(f'Успешно. Статус код - {response.status_code}')
        else:
            print(f'Ошибка. Статус код == {response.status_code}')

    @staticmethod
    def check_response_field(response, expected_value: list):
        """Метод проверки наличия полей в ответе сервера"""

        token = json.loads(response.text)
        assert list(token) == expected_value
        print('Все поля в ответе сервера присутсвуют')

    @staticmethod
    def check_response_value_field(response, field_name: str, expected_value: str):
        """Метод проверки значение заданного поля в ответе сервера"""

        check = response.json().get(field_name)
        assert check == expected_value
        print(f'Значение поля {field_name} верен!')
