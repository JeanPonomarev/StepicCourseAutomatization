link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_link(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
