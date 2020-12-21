from selenium.webdriver.common.by import By


class TestLocators:
    LOCATOR_FIRST_NAME = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[2]/td[2]/input")
    LOCATOR_LAST_NAME = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[3]//input")
    LOCATOR_CATEGORY_1 = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[4]//select")
    LOCATOR_CATEGORY_2 = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[4]/td[2]/select/option[3]")
    LOCATOR_CATEGORY_OPT = "//*[@id='gwt-debug-contentPanel']//tr[4]/td[2]/select/option["
    LOCATOR_BIRTHDAY = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[5]//input")
    LOCATOR_DATE = (By.XPATH, "//tr[2]//tr[5]/td[4]/div")
    LOCATOR_ADRESS = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[6]//textarea")
    LOCATOR_SCORE = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//td[1]/div[2]")
    LOCATOR_SCROLL = (By.XPATH, "//div[@class='GNHGC04CJJ']/div/div/div/div")
    LOCATOR_SMTH_CONTACT = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//div[3]//td[1]/div/div/div/div[1]")
    LOCATOR_SUBMIT = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[7]//button[2]")
    LOCATOR_UPDATE = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//tr[7]//button[1]")
    LOCATOR_GENERATE = (By.XPATH, "//*[@id='gwt-debug-contentPanel']//td[2]/button")
