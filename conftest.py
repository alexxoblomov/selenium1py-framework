import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en',
                         help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome()
        # chrome_path = Service("C:\\Work\\chromedriver-win64\\chromedriver.exe")
        # browser = webdriver.Chrome(service=chrome_path)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox()
        # firefox_path = Service('C:\\Program Files (x86)\\geckodriver\\geckodriver.exe')
        # browser = webdriver.Firefox(service=firefox_path, firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()