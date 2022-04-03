from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_button_add_to_basket(browser):
    browser.get(link)
    button_add_to_basket = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket')))

    assert button_add_to_basket, f'Страница товара на сайте {link} не содержит кнопки добавления в корзину'
