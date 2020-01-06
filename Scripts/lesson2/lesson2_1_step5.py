from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_css_selector("#input_value")
    x=x_element.text
    result=str(math.log(abs(12*math.sin(int(x)))))
    input1=browser.find_element_by_css_selector("#answer")
    input1.send_keys(result)
    checkbox1=browser.find_element_by_css_selector("#robotCheckbox")
    checkbox1.click()
    radio1=browser.find_element_by_css_selector("#robotsrule")
    radio1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
