"""
All locators here are announced as
'<button_name>_loc'
"""

# ya.ru - кнопки входа, логина, пароля и перехода в Диск
sign_in_loc = 'Войти'
change_to_email_loc = '[data-type="login]"'
login_loc = 'login'
sign_in_button_loc = 'passp:sign-in'
passw_field_loc = 'passwd'
skip_button_loc = '[data-t="button:pseudo"]'
avatar_button_loc = '[aria-label="Меню профиля, вход выполнен"]'
disk_button_appear_loc = 'Диск'

# disk.yandex.ru - создание папки, копирование файла в папку, выход из аккаунта
create_button_loc = 'span > button'
create_folder_button_loc = '[aria-label="Папку"]'
folder_name_field_loc = '[text="Новая папка"]'
save_folder_loc = '[class="dialog__body"] [type="button"]'
is_folder_saved_loc = '[aria-label="Тестовая папка для задания"]'
file_loc = '[aria-label="Файл для копирования.txt"]'
copy_button_appear_loc = '[value="copy"]'
copy_button_loc = '[class="Menu-Item Menu-Item_type_menuitem resources-actions-popup__action resources-actions-popup__action_type_copy"]'
destination_folder_loc = '[aria-label="Тестовая папка для задания Уровень 1 Закрыто Не выбрано"]'
confirm_copy_button_loc = 'button.Button2_view_action:nth-child(2)'
folder_loc = 'listing-item__fields'
file_in_folder_loc = '[title="Файл для копирования.txt"]'
folder_title_loc = '[title="Тестовая папка для задания"'
avatar_in_disk_loc = '[aria-label="Аккаунт"]'
logout_button_loc = '[aria-label="Выйти из аккаунта"]'

# disk.yandex.ru - загрузка и открытие файла, проверка текста внутри файла, текст для сравнения
is_folder_with_ast_saved_loc = '[title="Тестовая папка для задания со звёздочкой"]'
folder_with_ast_loc = '[aria-label="Тестовая папка для задания со звёздочкой"]'
upload_button_loc = '[type="file"]'
uploaded_file_loc = '[title="Файл для загрузки.txt"]'
close_popup_loc = '[aria-label="Закрыть"]'
is_uploaded_loc = 'uploader-progress__progress-primary'
text_in_file_loc = '[class="mg1"]:nth-child(1)'
close_notify_loc = '[aria-label="Отменить выделение"]'

expected_text = 'Здесь могла быть ваша реклама (или ваше приглашение меня на техническое собеседование)'
