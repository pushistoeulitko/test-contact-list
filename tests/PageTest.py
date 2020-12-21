from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.Base import BasePage
from tests.Locators import TestLocators
import allure


class Method(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_button(self, path):
        self.find_element(path, time=2).click()

    def type_text(self, path, mesege):
        field = self.find_element(path, time=2)
        field.clear()
        field.send_keys(mesege)

    def select_category(self, category):
        self.click_button(TestLocators.LOCATOR_CATEGORY_1)
        path = (By.XPATH, TestLocators.LOCATOR_CATEGORY_OPT + f"{category}]")
        self.click_button(path)

    def date_picker(self, date):
        self.click_button(TestLocators.LOCATOR_BIRTHDAY)
        if date == 0:
            self.click_button(TestLocators.LOCATOR_DATE)
        if date != 0:
            self.type_text(TestLocators.LOCATOR_BIRTHDAY, date)
            self.find_element(TestLocators.LOCATOR_BIRTHDAY).send_keys(Keys.ENTER)

    def check_number_contact(self, num, num0=30):
        a = self.find_element(TestLocators.LOCATOR_SCORE).text
        assert a == f"0 - {num0} : {num}", "не ОК"

    def fill_contact(self, first_name, last_name, address, date=0):
        try:
            self.type_text(TestLocators.LOCATOR_FIRST_NAME, first_name)
            self.type_text(TestLocators.LOCATOR_LAST_NAME, last_name)
            self.date_picker(date)
            self.type_text(TestLocators.LOCATOR_ADRESS, address)
            print(f"Форма корректно заполнена: {first_name} {last_name} {address}")
        except:
            print(f"! Форма не заполнена")

    def check_elements(self, plus_n):
        try:
            scroll_elem = self.find_element(TestLocators.LOCATOR_SCROLL)
            scroll_elem.send_keys(Keys.END)
            a = self.find_elements(TestLocators.LOCATOR_SCROLL)
            len(a)
            print(f"Найдено {len(a)} элементов")
        except:
            print(f"! Найдено {len(a)} элементов")
        assert len(a) == (252 + plus_n)

    @staticmethod
    def search_text_conf(first_name, last_name, address):
        if first_name == " ":
            search_text = f"{last_name}\n{address}"
            return search_text
        if last_name == " ":
            search_text = f"{first_name}\n{address}"
            return search_text
        if address == " ":
            search_text = f"{first_name} {last_name}"
            return search_text
        else:
            search_text = f"{first_name} {last_name}\n{address}"
            return search_text

    def check_search_elements(self, search_text, scroll):
        try:
            if scroll:
                scroll_elem = self.find_element(TestLocators.LOCATOR_SCROLL)
                scroll_elem.send_keys(Keys.END)
            a = self.find_elements(TestLocators.LOCATOR_SCROLL)
            for i in range(len(a) - 1):
                if a[i].text == search_text:
                    success = a[i].text
                    return success
                else:
                    continue
        except:
            print(f"нет текста {search_text}")
            assert False
        else:
            assert a[len(a) - 1].text == search_text

    def screenshots(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
