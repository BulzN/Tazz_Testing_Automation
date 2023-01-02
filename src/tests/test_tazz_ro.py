# test_tazz_ro

from src.pages.homepage import HomepageTazz
from src.utilities.ReportClass import ReportClass
from src.pages.tazz_intro_page import IntroPage
from src.pages.account_creation_tazz import AccountCreation
import pytest
import time


@pytest.mark.usefixtures("setup")
class TestTazz(ReportClass):

    # Test I - Testam functionalitatea site-ului prin introducerea unor date legate de utilizator despre unde să fie
    # servită comanda

    def test_1(self, setup):
        log = self.getLogger()
        homepage = HomepageTazz(self.driver)

        homepage.input_location_search()
        log.info("Input Address in order to search")
        time.sleep(1.756)

        homepage.input_data_address()
        log.info("Input first time supplementary info about address")
        time.sleep(1.756)

    # Testul II - Testăm selectarea anumitor produse introducandu-le in cos de la o anumita categorie de restaurant
    # introdusă de utilizator
    def test_2(self, setup):
        log = self.getLogger()
        intro_page = IntroPage(self.driver)

        intro_page.input_restaurant_search()
        log.info("Searching for the Restaurant 'Big Belly' & selecting it")
        time.sleep(3)

        intro_page.input_data_about_restaurant()
        log.info("Placing an order from the restaurant")
        time.sleep(1.765)

    # TEST III - Testâm căutarea unor altor produse pe pagina principală
    # alături de testarea coșului de cumpărături cu checkout

    def test_3(self,setup):
        log = self.getLogger()
        intro_page = IntroPage(self.driver)

        intro_page.other_acquisition()
        log.info("Trying to search for another product and going to the checkout")
        time.sleep(1.765)

    # TEST IV - Testăm funcționalitatea creării unui cont nou la cererea site-ului în momentul de checkout ( dar fără
    # să confirmăm contul, datorită numărului unic de verificare la nivel telefonic )
    def test_4(self, setup):
        log = self.getLogger()
        acc_creation = AccountCreation(self.driver)

        acc_creation.checkout_step()
        log.info("Confirming the checkout, but prompting on generation of a new account")
        time.sleep(1.765)

        acc_creation.human_verification()
        log.info("Confirming the human verification and going trough the process")
        time.sleep(1.765)

        acc_creation.introduce_data_account()
        log.info("Introducing data about account & finishing with the process")
        time.sleep(1.765)