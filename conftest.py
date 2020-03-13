from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = 'ru', help = 'Choose language: ')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    # browser.save_screenshot(f'Screenshots/Screenshot-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
    browser.quit()


