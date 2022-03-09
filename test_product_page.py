import pytest
from .pages.product_page import ProductPage
import time


links = [num if num != 7 else pytest.param(num, marks=pytest.mark.xfail) for num in range(10)]

@pytest.mark.parametrize('num', links)
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()