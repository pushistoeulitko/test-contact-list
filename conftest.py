import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    path = 'C://Users//pushi//PycharmProjects//'
    driver = webdriver.Chrome(executable_path=path + 'chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')
    yield driver
    print("\nquit browser..")
    driver.quit()
