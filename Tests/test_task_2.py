import unittest
import requests
from task_2 import created_folder


class TestCreatedFolder(unittest.TestCase):

    def test_created_folder(self):
        base_url = "https://cloud-api.yandex.net"
        url_get_information_folder = base_url + "/v1/disk/resources"
        token = ""
        headers = {"Authorization": token}
        params = {"path": "Test_1"}
        response = requests.get(url_get_information_folder, headers=headers, params=params)
        print(response.status_code)
        if response.status_code != 200:
            expected_result = 201
            result = created_folder("Test_1", token)
            self.assertEqual(expected_result, result)
        else:
            expected_result = 'По указанному пути "Test_1" уже существует папка с таким именем.'
            result = created_folder("Test_1", token)
            self.assertEqual(expected_result, result)


