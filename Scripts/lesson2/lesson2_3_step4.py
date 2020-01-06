#from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math
#import os

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    continue_button=browser.find_element_by_css_selector(".btn")
    continue_button.click()
    confirm=browser.switch_to.alert
    confirm.accept()
    x_element=browser.find_element_by_css_selector("#input_value")
    x=x_element.text
    result=str(math.log(abs(12*math.sin(int(x)))))
    result_input=browser.find_element_by_css_selector("input#answer")
    result_input.send_keys(result)
    submit_button=browser.find_element_by_css_selector(".btn-primary")
    submit_button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
