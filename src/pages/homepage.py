# Homepage - tazz.ro
# Prima vizita a utilizatorului către website, selectând deasemenea primele date importante legate de comanda acestuia
# (Personale)

from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver import Keys
import time


class HomepageTazz(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        # General Address Input First Time
        "input_address":
            ("CSS", "body > tz-landing > section.landing-address > div.la-address-contents.contents > tz-landing-location > tz-landing-address > div > div.location-search-box > div > input"),
        "continue_btn":
            ("XPATH", "/html/body/tz-landing/section[1]/div[2]/tz-landing-location/tz-landing-address/div/a"),
        "confirm_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[3]/div[2]"),
        "input_details_address":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[2]/div[2]/div/div[2]/textarea"),
        "home_type_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[2]/div[2]/div/div[4]/div[1]"),
        "save_address_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[2]/div[2]/div/div[5]/div")
    }

    def input_location_search(self):
        self.input_address.set_text("Strada Ceahlău 77, Cluj-Napoca")
        time.sleep(2)
        self.continue_btn.click()
        time.sleep(2)
        self.confirm_btn.click()
        time.sleep(2)

    def input_data_address(self):
        self.input_details_address.send_keys("Căminul V, Camera 31")
        time.sleep(2)
        self.home_type_btn.click()
        time.sleep(2)
        self.save_address_btn.click()
        time.sleep(2)
