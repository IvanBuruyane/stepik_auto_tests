from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
#import os

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    #browser.implicitly_wait(5)
    browser.get(link)

    price_element=WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    #price=price_element.text
    book_button=browser.find_element(By.ID,"book")
    book_button.click()
    
    x_element=browser.find_element_by_css_selector("#input_value")
    x=x_element.text
    result=str(math.log(abs(12*math.sin(int(x)))))
    result_input=browser.find_element_by_css_selector("input#answer")
    result_input.send_keys(result)
    submit_button=browser.find_element(By.ID,'solve') #WebDriverWait(browser,2).until(EC.element_to_be_clickable((By.ID,'submit')))
    submit_button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
