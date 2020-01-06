#from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
#import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input=browser.find_element_by_css_selector("input[name='firstname']")
    first_name_input.send_keys("Ali")
    last_name_input=browser.find_element_by_css_selector("input[name='lastname']")
    last_name_input.send_keys("Baba")
    email_input=browser.find_element_by_css_selector("input[name='email']")
    email_input.send_keys("email")
    file_input=browser.find_element_by_css_selector("input#file")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'lesson2_2_step8_file.txt')

    file_input.send_keys(file_path)

    submit_button=browser.find_element_by_css_selector(".btn")
    submit_button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
