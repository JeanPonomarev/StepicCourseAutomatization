from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_element = browser.find_element_by_id("treasure")
    treasure_value = treasure_element.get_attribute("valuex")

    result = calc(treasure_value)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()

    submit_button = browser.find_element_by_class_name("btn.btn-default")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
