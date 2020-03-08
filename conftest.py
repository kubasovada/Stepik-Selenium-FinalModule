from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = 'ru', help = 'Choose language: en or rus or es or the other')

@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language}"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(link)
    yield browser
    browser.quit()


