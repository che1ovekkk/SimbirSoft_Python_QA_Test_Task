from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from credentials import login, password
import allure


@allure.step('Открытие браузера')
def open_browser(url):
    browser = webdriver.Chrome()
    browser.get(url=url)
    return browser


@allure.title('Создание папки и копирование файла в созданную папку на Яндекс.Диске')
def test_copy_file():
    # В задании указано пройти по адресу 'yandex.ru', но по нему идёт редирект на dzen.ru
    # Поэтому в задании использовал актуальный адрес поисковика
    browser = open_browser(url='http://ya.ru')

    with allure.step('Нажатие кнопки "Войти"'):
        sign_in_button = browser.find_element(By.LINK_TEXT, sign_in_loc)
        sign_in_button.click()

    with allure.step('Заполнение данных для входа'):
        try:
            with allure.step('Переключение на вкладку логина по почте'):
                change_to_email = browser.find_element(By.CSS_SELECTOR, change_to_email_loc)
                change_to_email.click()
        except:
            pass

        with allure.step('Ввод логина'):
            login_field = browser.find_element(By.NAME, login_loc)
            login_field.send_keys(login)
            sign_in_button = browser.find_element(By.ID, sign_in_button_loc)
            sign_in_button.click()

        with allure.step('Ввод пароля'):
            passw_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, passw_field_loc)))
            passw_field.send_keys(password)
            sign_in_button = browser.find_element(By.ID, sign_in_button_loc)
            sign_in_button.click()

        with allure.step('Пропуск привязки телефона'):
            try:
                skip_button = browser.find_element(By.CSS_SELECTOR, skip_button_loc)
                skip_button.click()
            except:
                pass

    with allure.step('Клик по аватарке и выбор Диска'):
        avatar_button_appear = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, avatar_button_loc)))
        avatar_button = browser.find_element(By.CSS_SELECTOR, avatar_button_loc)
        avatar_button.click()
        disk_button_appear = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, disk_button_appear_loc)))
        disk_button = browser.find_element(By.LINK_TEXT, disk_button_appear_loc)
        disk_button.click()

    with allure.step('Создание папки'):
        browser.switch_to.window(browser.window_handles[1])
        create_button = browser.find_element(By.CSS_SELECTOR, create_button_loc)
        create_button.click()
        create_folder_button = browser.find_element(By.CSS_SELECTOR, create_folder_button_loc)
        create_folder_button.click()

        with allure.step('Заполняем название создаваемой папки'):
            folder_name_field = browser.find_element(By.CSS_SELECTOR, folder_name_field_loc)
            folder_name_field.click()
            ActionChains(browser).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
                Keys.BACKSPACE).perform()
            folder_name_field.send_keys('Тестовая папка для задания')

        with allure.step('Сохраняем созданную папку'):
            save_folder = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, save_folder_loc)))
            save_folder.click()
            is_folder_saved = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, is_folder_saved_loc)))

    with allure.step('Копируем файл в папку'):
        with allure.step('Поиск файла и ПКМ на него'):
            file = browser.find_element(By.CSS_SELECTOR, file_loc)
            ActionChains(browser).context_click(file).perform()
            copy_button_appear = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, copy_button_appear_loc)))
            copy_button = browser.find_element(By.CSS_SELECTOR, copy_button_loc)
            ActionChains(browser).click(copy_button).perform()

        with allure.step('Выбор папки для перемещения'):
            destination_folder_await = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, destination_folder_loc)))
            destination_folder = browser.find_element(By.CSS_SELECTOR, destination_folder_loc)
            ActionChains(browser).click(destination_folder).perform()
            confirm_copy_button = browser.find_element(By.CSS_SELECTOR, confirm_copy_button_loc)
            ActionChains(browser).click(confirm_copy_button).perform()

    with allure.step('Открытие папки с файлом'):
        folder = browser.find_element(By.CLASS_NAME, folder_loc)
        ActionChains(browser).double_click(folder).perform()

    with allure.step('Проверка наличия файла'):
        file_in_folder_await = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, file_in_folder_loc)))
        file_in_folder = browser.find_element(By.CSS_SELECTOR, file_in_folder_loc)
        file_name = file_in_folder.get_attribute("title")
        folder_title = browser.find_element(By.CSS_SELECTOR, folder_title_loc).text

    try:
        assert (folder_title, file_name) == ('Тестовая папка для задания', 'Файл для копирования.txt')
    finally:
        with allure.step('Выход из аккаунта и закрытие браузера'):
            avatar_in_disk = browser.find_element(By.CSS_SELECTOR, avatar_in_disk_loc)
            avatar_in_disk.click()
            logout_button = browser.find_element(By.CSS_SELECTOR, logout_button_loc)
            logout_button.click()
            browser.quit()
