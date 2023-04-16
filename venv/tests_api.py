import allure
import requests
from urls_for_api import *

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'OAuth y0_AgAAAABp9juuAAm2yAAAAADhD5kFNLZdroOhTYqOZCnIAL8_tQrFr1I',
}

@allure.title('Создание папки, копирвоание в неё файла и переименование файла в папке')
def test_api():
    with allure.step('Создание папки'):
        create_folder = requests.put(url_to_create_folder, headers=headers)

    with allure.step('Копирование файла'):
        copy_file_to_folder = requests.post(url_to_copy_file, headers=headers)

    with allure.step('Переименование файла'):
        rename_file = requests.post(url_to_rename_file, headers=headers)

    with allure.step('Подготовка данных для проверки'):
        check_renamed_file = requests.get(url_to_check_renamed_file, headers=headers)
        content = str(check_renamed_file.content)

    assert (rename_file.status_code, content.__contains__('RenamedFileToCopy.txt'),
            rename_file.headers.get('content-type')) == (201, True, 'application/json; charset=utf-8')
