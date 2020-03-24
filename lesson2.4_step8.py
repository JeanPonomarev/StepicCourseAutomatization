from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calculate(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    result = calculate(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(result))

    submit_button = browser.find_element_by_id("solve")
    submit_button.click()
finally:
    time.sleep(5)
    browser.quit()