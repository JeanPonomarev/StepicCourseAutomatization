from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()

    submit_button = browser.find_element_by_class_name("btn.btn-default")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
