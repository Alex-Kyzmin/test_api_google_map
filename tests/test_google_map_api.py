import allure

from utils.api import GoogleMapsAPI
from utils.checking import Checking


@allure.epic('Test API Google Maps')
class TestGoogleMapAPI:
    """
    Класс тестов API сервиса Google Maps API
    https://rahulshettyacademy.com
    """

    @allure.description('Tests http-methods')
    def test_http_methods(self):
        """Тестировоание HTTP-methods"""

        print('Тестирование HTTP-метода "POST" - создание локации')
        response_post = GoogleMapsAPI.create_location()
        Checking.check_status_code(
            response=response_post,
            expected_status_code=200,
        )
        place_id = response_post.json().get('place_id')
        print('Возможность создание локации проверена.')

        print('Тестирование HTTP-метода "GET" - получение информации о локации')
        response_get = GoogleMapsAPI.get_location_value(place_id)
        Checking.check_status_code(
            response=response_get,
            expected_status_code=200,
        )
        list_expected_fields = ['location', 'accuracy', 'name', 'phone_number',
                                'address', 'types', 'website', 'language']
        Checking.check_response_field(
            response=response_get,
            expected_value=list_expected_fields
        )
        Checking.check_response_value_field(
            response=response_get,
            field_name='address',
            expected_value='29, side layout, cohen 09'
        )
        print('Возможность получения информации о локации по id проверена.')

        print('Тестирование HTTP-метода "PUT" - изменение адреса локации')
        response_put = GoogleMapsAPI.update_location(place_id)
        Checking.check_status_code(
            response=response_put,
            expected_status_code=200,
        )
        Checking.check_response_field(
            response=response_put,
            expected_value=['msg']
        )
        print('Возможность изменения локации проверена.')

        print('Тестирование HTTP-метода "DELETE" - удаление локации')
        response_delete = GoogleMapsAPI.delete_location(place_id)
        Checking.check_status_code(
            response=response_delete,
            expected_status_code=200,
        )
        Checking.check_response_value_field(
            response=response_delete,
            field_name='status',
            expected_value='OK'
        )
        print('Возможность удаления локации проверена.')
