from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    robots_radio = browser.find_element_by_id("robotsRule")

    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio:", robots_checked)
    assert robots_checked is not None

finally:
    time.sleep(3)
    browser.quit()