import pytest
import time
from selenium import webdriver

def test_add_to_basket_button_exists(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket_button=browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert add_to_basket_button,"There is no ADD_TO_BASKET_BUTTON on the page"
    time.sleep(30)



