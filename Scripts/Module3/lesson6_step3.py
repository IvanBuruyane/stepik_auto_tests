import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('numbers', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_parametrization(browser, numbers):
    link = f"https://stepik.org/lesson/{numbers}/step/1"
    browser.get(link)
    textarea=browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))
    browser.find_element_by_css_selector("button.submit-submission").click()
    aliens_text=browser.find_element_by_css_selector("pre.smart-hints__hint").text
    assert aliens_text=="Correct!", f"Aliens text is '{aliens_text}'"