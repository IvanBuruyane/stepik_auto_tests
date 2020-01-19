from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
browser=webdriver.Chrome()

def test_guest_should_see_login_link_pass():
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail():
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
