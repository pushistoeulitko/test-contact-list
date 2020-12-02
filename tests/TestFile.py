import pytest
from tests.Locators import TestLocators
from tests.PageTest import Method

fn = 'Juliette'
ln = 'has a gan'
ad = 'gan'
big_string = 1234567890123456789012345678901234567890  # 40
short_string = 1


@pytest.mark.parametrize("first_name", ['Juliette', '12345', '###', big_string, short_string])
def test_one_field_first_name(browser, first_name):
    page = Method(browser)
    page.fill_contact(first_name, ln, ad)
    page.click_button(TestLocators.LOCATOR_SUBMIT)
    page.screenshots()
    page.check_number_contact(251)


@pytest.mark.parametrize("last_name", ['Juliette', '12345', '###'])
def test_one_field_last_name(browser, last_name):
    page = Method(browser)
    page.fill_contact(fn, last_name, ad)
    page.click_button(TestLocators.LOCATOR_SUBMIT)
    page.screenshots()
    page.check_number_contact(251)


@pytest.mark.parametrize("address", ['Juliette', '12345', '###'])
def test_one_field_last_name(browser, address):
    page = Method(browser)
    page.fill_contact(fn, ln, address)
    page.click_button(TestLocators.LOCATOR_SUBMIT)
    page.screenshots()
    page.check_number_contact(251)


@pytest.mark.parametrize("category", ['1', '2', '3', '4', '5'])
def test_one_field_select_category(browser, category):
    pytest.skip()
    page = Method(browser)
    #LOCATOR_CATEGORY_OPT
    page.fill_contact(fn, ln, ad)
    page.select_category()
    page.click_button(TestLocators.LOCATOR_SUBMIT)
    page.check_number_contact(251)


@pytest.mark.parametrize("date", ['December 22, 2020', '22.12.2020', '12345', '###'])
def test_one_field(browser, date):
    pytest.skip()
    page = Method(browser)
    page.fill_contact(fn, ln, ad, date)
    page.click_button(TestLocators.LOCATOR_SUBMIT)
    page.check_number_contact(251)


@pytest.fixture(scope="function", params=[
    ("Juliette", "has a gan", "gan"),
    (" ", "has a gan", "gan"),
    ("Juliette", " ", "gan"),
    ("Juliette", "has a gan", " ")],
                ids=["full", "no first_name", "no last_name", "no address"])
def param_test(request):
    return request.param


def test_create_contact(browser, param_test):
    (first_name, last_name, address) = param_test
    page = Method(browser)
    page.fill_contact(first_name, last_name, address)
    page.click_button(TestLocators.LOCATOR_SUBMIT)
    page.check_number_contact(251)
    page.screenshots()
    search_text = page.search_text_conf(first_name, last_name, address)
    page.check_search_elements(search_text, True)


def test_update_contact(browser, param_test):
    page = Method(browser)
    (first_name, last_name, address) = param_test
    page.click_button(TestLocators.LOCATOR_SMTH_CONTACT)
    page.fill_contact(first_name, last_name, address)
    page.click_button(TestLocators.LOCATOR_UPDATE)
    page.check_number_contact(250)
    page.screenshots()
    search_text = page.search_text_conf(first_name, last_name, address)
    page.check_search_elements(search_text, False)


def test_generate_contacts(browser):
    page = Method(browser)
    page.click_button(TestLocators.LOCATOR_GENERATE)
    page.screenshots()
    page.check_number_contact(300)
    page.check_elements(50)
