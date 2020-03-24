from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    first_name_field.send_keys("Ivan")

    second_name_field = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    second_name_field.send_keys("Petrov")

    email_field = browser.find_element_by_css_selector("[placeholder='Enter email']")
    email_field.send_keys("xxx@gmail.com")

    # отправка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "File.txt")

    file_sender = browser.find_element_by_id("file")
    file_sender.send_keys(file_path)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()