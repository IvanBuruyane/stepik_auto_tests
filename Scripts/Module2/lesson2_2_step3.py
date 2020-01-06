from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element=browser.find_element_by_css_selector("#num1")
    num2_element=browser.find_element_by_css_selector("#num2")
    num1=num1_element.text
    num2=num2_element.text
    result=str(int(num1)+int(num2))
    select1=Select(browser.find_element_by_css_selector("#dropdown"))
    select1.select_by_value(result)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
