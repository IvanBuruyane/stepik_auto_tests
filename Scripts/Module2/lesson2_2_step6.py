#from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_css_selector("#input_value")
    x=x_element.text
    result=str(math.log(abs(12*math.sin(int(x)))))
    input1=browser.find_element_by_css_selector("#answer")
    input1.send_keys(result)
    check1=browser.find_element_by_css_selector("#robotCheckbox")
    check1.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radio1=browser.find_element_by_css_selector("#robotsRule")
    radio1.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
