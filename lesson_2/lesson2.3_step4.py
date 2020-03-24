from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def function(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element_by_class_name("btn.btn-primary")
    first_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    result = function(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(result))

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
