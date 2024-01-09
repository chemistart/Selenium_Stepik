from selenium.webdriver.common.by import By
import time

def test_find_basket_button(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    #time.sleep(30)

    basket_button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert basket_button, "The add to cart button wasn't found"
