from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    result = calculate(x)

    answer_element = browser.find_element_by_id("answer")
    answer_element.send_keys(result)

    browser.execute_script("window.scrollBy(0, 100);")

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robot_radiobutton = browser.find_element_by_id("robotsRule")
    robot_radiobutton.click()

    submit_button = browser.find_element_by_class_name("btn.btn-primary")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
