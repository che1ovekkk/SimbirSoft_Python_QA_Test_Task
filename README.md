Тестовое задание на QA Engineer Fullstack (Python).
Локаторы собраны в файле locators.py.
URL-адреса для API-теста собраны в файле urls_for_api.py.
Зависимости зафиксированы в файле  requirements.txt.

Использован Allure для генерации отчётов

*****
Перед запуском тестов нужно создать в проекте файл credetials.py и внести в него строковые переменные login, password и token, 
а также заполнить эти переменные соответствующими значениями, переданными в письме.
*****

Для запуска тестов нужно скачать проект и в терминале выполнить команду "pytest -v file_with_tests.py --alluredir=/tmp/my_allure_results", 
где "file_with_tests.py" нужно заменить на имя файла нужного теста.

Для просмотра allure-отчёта нужно выполнить команду "allure serve /tmp/my_allure_results"
