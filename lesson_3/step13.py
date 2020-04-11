import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")

            input1 = browser.find_element_by_css_selector('input[class="form-control first"][required]')
            input1.send_keys("Ivan")

            input2 = browser.find_element_by_css_selector('input[class="form-control second"][required]')
            input2.send_keys("Petrov")

            input3 = browser.find_element_by_css_selector('input[class="form-control third"][required]')
            input3.send_keys("ivan@gmail.com")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            time.sleep(10)
            browser.quit()

    def test_2(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")

            input1 = browser.find_element_by_css_selector('input[class="form-control first"][required]')
            input1.send_keys("Ivan")

            input2 = browser.find_element_by_css_selector('input[class="form-control second"][required]')
            input2.send_keys("Petrov")

            input3 = browser.find_element_by_css_selector('input[class="form-control third"][required]')
            input3.send_keys("ivan@gmail.com")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            time.sleep(10)
            browser.quit()


if __name__ == "__main__":
    unittest.main()