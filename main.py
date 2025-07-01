# Sprint 8 Test File
import pages
import data
import helpers
from selenium  import webdriver

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        helpers.is_url_reachable(data.URBAN_ROUTES_URL)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to Urban Routes Server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert page.get_from_location() == data.ADDRESS_FROM
        assert page.get_to_location() == data.ADDRESS_TO


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        assert "active" in page.get_is_supportive_option_selected()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        page.click_phone_number_button()
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_phone_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        page.enter_sms_code(code)
        page.click_code_confirm_button()
        assert page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        page.click_payment_method_button()
        page.click_add_card_option()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.click_card_link_button()
        assert page.get_card_option()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        page.click_order_blanket_handkerchiefs_toggle()
        assert page.get_order_blanket_handkerchiefs_toggle() == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        page.click_icecream_add_button()
        assert page.get_icecream_order_counter() == '2'

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = pages.UrbanRoutesPage(self.driver)
        page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_custom_option()
        page.click_call_a_taxi()
        page.click_supportive_option()
        page.click_payment_method_button()
        page.click_add_card_option()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.click_card_link_button()
        page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        page.click_order_blanket_handkerchiefs_toggle()
        page.click_icecream_add_button()
        page.click_enter_number_and_order_button()
        assert page.test_driver_will_arrive()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()