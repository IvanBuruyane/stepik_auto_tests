from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_lesson6_step10(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_name=browser.find_element_by_css_selector("input.first:required")
            first_name.send_keys("FirstName")
            last_name=browser.find_element_by_css_selector("input.second:required")
            last_name.send_keys("LastName")
            email=browser.find_element_by_css_selector("input.third:required")
            email.send_keys("email")
            phone=browser.find_element_by_css_selector(".second_block input.first")
            phone.send_keys("+32342342342")
            adress=browser.find_element_by_css_selector(".second_block input.second")
            phone.send_keys("adress")
            
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text,"Congratulations! You have successfully registered!","Something went wrong")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_lesson6_step11(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        first_name=browser.find_element_by_css_selector("input.first:required")
        first_name.send_keys("FirstName")
        last_name=browser.find_element_by_css_selector("input.second:required")
        last_name.send_keys("LastName")
        email=browser.find_element_by_css_selector("input.third:required")
        email.send_keys("email")
        phone=browser.find_element_by_css_selector(".second_block input.first")
        phone.send_keys("+32342342342")
        adress=browser.find_element_by_css_selector(".second_block input.second")
        phone.send_keys("adress")
            
            # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        time.sleep(2)

            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!","Something went wrong")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
