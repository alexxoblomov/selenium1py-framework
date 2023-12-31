import time
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize('link',
["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
              marks=pytest.mark.xfail),
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """
    1) Открываем страницу
    2) Добавляем товар в корзину
    3) Даем ответ на задачу и подтверждаем все алерты
    4) Смотрим, что название книги на витрине и в сообщении о добавлении совпадают
    5) Смотрим, что цена на витрине и в сообщении о добавлении в корзину совпадают
    """
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.book_names_is_match()
    page.book_prices_is_match()


@pytest.mark.negative
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    1) Открываем страницу
    2) Добавляем товар в корзину
    3) Ожидаем, что сообщение об успешном добавлении не появилось
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.no_message_about_adding()


@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    """
    1) Открываем страницу
    2) Ожидаем, что сообщение об успешном добавлении не появилось
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)

    page.open()
    page.no_message_about_adding()


@pytest.mark.negative
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1) Открываем страницу
    2) Добавляем в корзину
    3) Ожидаем, что сообщение о добавлении пропадает со временем
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()
    page.message_about_adding_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    1) Открываем страницу
    2) Смотрим, что есть ссылка на страницу логина
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)

    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    1) Открываем страницу
    2) Смотрим, что можем перейти на страницу логина
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)

    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    1) Открываем страницу
    2) Переходим в корзину по кнопке в шапке
    3) Ожидаем, что в корзине нет товаров
    4) Ожидаем, что есть текст о том, что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)

    page.open()
    page.go_to_basket()
    page.is_basket_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "54321"
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        1) Открываем страницу
        2) Ожидаем, что сообщение об успешном добавлении не появилось
        """
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)

        page.open()
        page.no_message_about_adding()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        1) Открываем страницу
        2) Добавляем товар в корзину
        3) Даем ответ на задачу и подтверждаем все алерты
        4) Смотрим, что название книги на витрине и в сообщении о добавлении совпадают
        5) Смотрим, что цена на витрине и в сообщении о добавлении в корзину совпадают
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)

        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.book_names_is_match()
        page.book_prices_is_match()
