import pytest
from selenium import webdriver
import time
import math

# answer = math.log(int(time.time()))

links_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture()
def time_answer():
    time_answer = math.log(int(time.time()))
    yield time_answer


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    yield browser
    browser.quit()


@pytest.mark.parametrize("links_list", [
    links_list[0], links_list[1], links_list[2], links_list[3],
    links_list[4], links_list[5], links_list[6], links_list[7]])
def test_correct_answer(browser, time_answer, links_list):
    link = links_list
    browser.get(link)

    test_field = browser.find_element_by_css_selector("[placeholder='Напишите ваш ответ здесь...']")

    test_field.send_keys(str(time_answer))

    submit_button = browser.find_element_by_class_name("submit-submission")
    submit_button.click()

    feedback = browser.find_element_by_class_name("smart-hints__hint")
    feedback_text = feedback.text

    assert feedback_text == "Correct!", "Feedback is wrong"
