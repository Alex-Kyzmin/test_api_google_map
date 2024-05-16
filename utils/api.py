from utils.send_method import SendMethod as Send


# базовая url
base_url = "https://rahulshettyacademy.com"

# ресурс для CREATE method
post_resource = "/maps/api/place/add/json"
# ресурс для READ method
get_resource = "/maps/api/place/get/json"
# ресурс для UPDATE method
put_resource = "/maps/api/place/update/json"
# ресурс для DELETE method
delete_resource = "/maps/api/place/delete/json"

# параметр для всех ресурсов
key = "?key=qaclick123"
# дополнительный параметр url для READ method
extra_arg = "&place_id="


class GoogleMapsAPI:
    """
    Класс взаимодействия с сервиса Google Maps API
    https://rahulshettyacademy.com
    """

    @staticmethod
    def create_location():
        """Method создания новой локации"""

        # тело POST-запроса для create method
        data_post = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = base_url + post_resource + key

        response_post = Send.create(
            url=post_url,
            data=data_post
        )

        return response_post

    @staticmethod
    def get_location_value(place_id: str):
        """Method получения информации о локации по id"""

        get_url = base_url + get_resource + key + extra_arg + place_id
        response_get = Send.read(
            url=get_url
        )

        return response_get

    @staticmethod
    def update_location(place_id: str):
        """Method изменения локации"""

        put_url = base_url + put_resource + key

        # тело PUT-запроса для update method
        data_put = {
            "place_id": place_id,
            "address": "40 Toreza street, RU",
            "key": "qaclick123"
        }

        response_put = Send.update(
            url=put_url,
            data=data_put,
        )

        return response_put

    @staticmethod
    def delete_location(place_id: str):
        """Method удаления локации"""

        delete_url = base_url + delete_resource + key

        # тело DELETE-запроса для delete method
        data_delete = {
            "place_id": place_id
        }

        response_delete = Send.delete(
            url=delete_url,
            data=data_delete,
        )

        return response_delete
