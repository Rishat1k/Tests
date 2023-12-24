import requests


token_yandex = ""

def created_folder(path, token):
    base_url = "https://cloud-api.yandex.net"
    url_for_creating_folder = base_url + "/v1/disk/resources"
    headers = {"Authorization": token}
    params = {"path": path}
    response = requests.put(url_for_creating_folder, headers=headers, params=params)
    if response.status_code < 300:
        print(f'Папка {path} создана')
        return response.status_code
    else:
        print(f'Папка {path} не создана: {response.json()["message"]}')
        return response.json()["message"]

if __name__ == '__main__':
    token = ''
    created_folder('Test_1', token)
