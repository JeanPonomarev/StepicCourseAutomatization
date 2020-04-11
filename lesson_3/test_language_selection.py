import time

link = "https://www.nsu.ru/n/"


def test_language_change_at_nsu(browser):
    browser.get(link)

    time.sleep(7)
