# test_tazz_ro

from src.pages.homepage import HomepageTazz
from src.utilities.ReportClass import ReportClass
from src.pages.tazz_intro_page import IntroPage
import pytest
import time


@pytest.mark.usefixtures("setup")
class TestTazz(ReportClass):

    # Test I - Testam functionalitatea site-ului prin introducerea unor date legate de utilizator
    # alaturi de selectarea anumitor produse introducandu-le in cos de la o anumita categorie de restaurant introduse
    # de utilizator

    def test_1(self, setup):
        log = self.getLogger()
        homepage = HomepageTazz(self.driver)

        homepage.input_location_search()
        log.info("Input Address in order to search")
        time.sleep(1.756)

        homepage.input_data_address()
        log.info("Input first time supplementary info about address")
        time.sleep(1.756)

        intro_page= IntroPage(self.driver)

        intro_page.input_restaurant_search()
        log.info("Searching for the Restaurant 'Big Belly' & selecting it")
        time.sleep(3)

        intro_page.input_data_about_restaurant()
        log.info("Placing an order from the restaurant")
        time.sleep(1.765)


    # # TEST II -

    # def test_2(self, setup):
    #     log = self.getLogger()