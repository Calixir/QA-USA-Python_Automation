# Sprint 8 Test File
import pages
import data
import helpers
from selenium  import webdriver
import time

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        helpers.is_url_reachable(data.URBAN_ROUTES_URL)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL) == True:
            print('Connected to Urban Routes Server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        time.sleep(1)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        time.sleep(1)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        time.sleep(1)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)
        page.click_phone_number_button()
        time.sleep(1)
        page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(1)
        page.click_phone_next_button()
        time.sleep(1)
        page.enter_sms_code('1111')
        time.sleep(1)
        page.click_code_confirm_button()
        time.sleep(1)

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        time.sleep(1)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)
        page.click_payment_method_button()
        time.sleep(1)
        page.click_add_card_option()
        time.sleep(1)
        page.enter_card_number(data.CARD_NUMBER)
        time.sleep(1)
        page.enter_card_code(data.CARD_CODE)
        time.sleep(2)
        page.click_card_link_button()
        time.sleep(1)

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)
        page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        assert page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)
        page.click_order_blanket_handkerchiefs_toggle()
        time.sleep(1)
        assert page.get_order_blanker_handkerchiefs_toggle() == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)
        page.click_icecream_add_button()
        time.sleep(1)
        page.click_icecream_add_button()
        time.sleep(1)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        page.click_custom_option()
        time.sleep(1)
        page.click_call_a_taxi()
        time.sleep(1)
        page.click_supportive_option()
        time.sleep(1)
        page.click_payment_method_button()
        time.sleep(1)
        page.click_add_card_option()
        time.sleep(1)
        page.enter_card_number(data.CARD_NUMBER)
        time.sleep(1)
        page.enter_card_code(data.CARD_CODE)
        time.sleep(2)
        page.click_card_link_button()
        time.sleep(1)
        page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        page.click_order_blanket_handkerchiefs_toggle()
        time.sleep(1)
        page.click_icecream_add_button()
        time.sleep(1)
        page.click_icecream_add_button()
        time.sleep(1)
        page.click_enter_number_and_order_button()
        time.sleep(5)
        assert page.test_driver_will_arrive() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()