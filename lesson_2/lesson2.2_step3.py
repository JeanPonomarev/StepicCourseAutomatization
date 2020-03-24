from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)

    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)

    result = x + y

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(result))

    button = browser.find_element_by_class_name("btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()
