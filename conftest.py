from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = 'ru', help = 'Choose language: ')
    parser.addoption('--browser', action = 'store', default = 'Chrome', help = 'Choose browser')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "Chrome":
        browser = webdriver.Chrome(options=options)
    elif browser_name == "Firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser name should be Chrome or Firefox")
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    # browser.save_screenshot(f'Screenshots/Screenshot-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    browser.quit()


