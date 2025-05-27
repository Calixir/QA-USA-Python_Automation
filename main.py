import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        helpers.is_url_reachable(data.URBAN_ROUTES_URL)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL) == True:
            print('Connected to Urban Routes Server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')
    def test_set_route(self):
        # Add in S8
        print("test_set_route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("test_select_plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("test_fill_phone_number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("test_fill_card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("test_comment_for_driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("test_order_blanket_and_handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        for i in range(2):
            # Add in S8
            print("Icecream x{i}")
            pass


    def test_car_search_model_appears(self):
        # Add in S8
        print("test_car_search_model_appears")
        pass

