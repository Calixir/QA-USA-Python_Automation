# Sprint 8 POM File
from dataclasses import field

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, "//div[@class='mode' and text()='Custom']")
    CALL_A_TAXI_LOCATOR = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_OPTION_LOCATOR = (By.XPATH, '//div[contains(text(),"Supportive")]//..')
    PHONE_NUMBER_BUTTON_LOCATOR = (By.XPATH, "//div[@class='np-text']")
    PHONE_NUMBER_LOCATOR = (By.ID, 'phone')
    PHONE_NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit' and text()='Next']")
    SMS_CODE_LOCATOR = (By.ID, 'code')
    CODE_CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit' and text()='Confirm']")
    PAYMENT_METHOD_BUTTON_LOCATOR = (By.XPATH, "//div[@class='pp-text']")
    ADD_CARD_OPTION_LOCATOR = (By.XPATH, "//img[@src='/static/media/plus.d25b8941.svg']")
    CARD_NUMBER_LOCATOR = (By.CLASS_NAME, "card-input")
    CARD_CODE_LOCATOR = (By.NAME, "code")
    # Maybe TAB locator here ...?
    CARD_LINK_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Link")]')
    CLOSE_BUTTON_PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    MESSAGE_FOR_DRIVER_LOCATOR = (By.ID, 'comment')
    ORDER_BLANKET_HANDKERCHIEFS_TOGGLE_LOCATOR = (By.XPATH, "//span[@class='slider round']")
    ICECREAM_ADD_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'counter-plus')]")
    ENTER_NUMBER_AND_ORDER_BUTTON_LOCATOR = (By.CLASS_NAME, 'smart-button-wrapper')
    DRIVER_WILL_ARRIVE_LOCATOR = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def enter_locations(self,from_text, to_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_call_a_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI_LOCATOR).click()

    def click_supportive_option(self):
        self.driver.find_element(*self.SUPPORTIVE_OPTION_LOCATOR).click()
        if self.driver.find_element(*self.SUPPORTIVE_OPTION_LOCATOR).get_attribute("class") != "tcard active":
            card= WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.SUPPORTIVE_OPTION_LOCATOR))
            self.driver.execute_script("arguments[0].scrollIntoView();", card)
            card.click()

    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON_LOCATOR).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(phone_number)

    def click_phone_next_button(self):
        self.driver.find_element(*self.PHONE_NEXT_BUTTON_LOCATOR).click()

    def enter_sms_code(self, sms_code_text):
        self.driver.find_element(*self.SMS_CODE_LOCATOR).send_keys(sms_code_text)

    def click_code_confirm_button(self):
        self.driver.find_element(*self.CODE_CONFIRM_BUTTON_LOCATOR).click()

    def click_payment_method_button(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON_LOCATOR).click()

    def click_add_card_option(self):
        self.driver.find_element(*self.ADD_CARD_OPTION_LOCATOR).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    def enter_card_code(self, card_code):
        field = self.driver.find_element(*self.CARD_CODE_LOCATOR)
        field.send_keys(card_code)
        field.send_keys(Keys.TAB)

    def click_card_link_button(self):
        self.driver.find_element(*self.CARD_LINK_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.CLOSE_BUTTON_PAYMENT_METHOD_LOCATOR).click()

    def enter_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER_LOCATOR).send_keys(message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER_LOCATOR).get_property('value')

    def click_order_blanket_handkerchiefs_toggle(self):
        self.driver.find_element(*self.ORDER_BLANKET_HANDKERCHIEFS_TOGGLE_LOCATOR).click()

    def get_order_blanker_handkerchiefs_toggle(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and contains(@class, 'switch-input')]")
        return checkbox.is_selected()

    def click_icecream_add_button(self):
        self.driver.find_element(*self.ICECREAM_ADD_BUTTON_LOCATOR).click()

    def click_enter_number_and_order_button(self):
        self.driver.find_element(*self.ENTER_NUMBER_AND_ORDER_BUTTON_LOCATOR).click()

    def test_driver_will_arrive(self):
        text = self.driver.find_element(*self.DRIVER_WILL_ARRIVE_LOCATOR)
        time.sleep(35)
        return text.is_displayed()
