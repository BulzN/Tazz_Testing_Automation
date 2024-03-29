# Tazz_Intro_Page.py - Prima Pagina de acum înainte, unde s-au salvat cookies-urile despre utilizator
# Selectând restaurante și alte cazuri pentru a face test-case-uri.
# Cu trecerea timpului, acest modul .py va fi îmbunătățit, introducând mai multe metode abstracte/generale alături de
# diverși locatori unici de identificare

from selenium.webdriver.common.action_chains import ActionChains
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver import Keys
import time


class IntroPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        # General Search Button
        "search_btn":
            ("XPATH",
             "/html/body/header/tz-header-box/div/div[1]/tz-search-box/div[1]/div[2]/input"),
        # General Input Text
        "input_search_txt":
            ("XPATH", "/html/body/tz-panel-search/div[1]/div/div[2]/div[2]/input"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "select_big_belly_txt":
            ("XPATH", "/html/body/header/tz-header-box/div/div[1]/tz-search-box/div[1]/div[3]/div[1]/div[1]"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "select_big_belly_btn":
            ("XPATH", "//*[@id='restaurants']/div/div/div[2]/div/div/div/div/div[2]"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "reference_pizza":
            ("XPATH", "//*[@id='subcategory-13005-product-133422']/div/div"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "choose_belly":
            ("XPATH", "//*[@id='subcategory-13005-product-133426']/div/div"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "second_reference_pizza":
            ("XPATH",
             "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[3]/div[1]/div[3]/div[8]/div[1]/label/span"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "choose_second_belly":
            ("XPATH",
             "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[3]/div[1]/div[3]/div[11]/div[1]/label"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "select_final_both_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 2
        "back_to_menu":
            ("XPATH", "/html/body/tz-dialog/div[1]"),
        # General Intro Page BTN
        "intro_page_btn":
            ("XPATH", "/html/body/header/tz-header-box/div/div[1]/div/a"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 3
        "select_other_btn":
            ("XPATH",
             "/html/body/div[2]/main/div/tz-widget-partner-types/div/div[2]/div/tz-dynamic-carousel/div/section/ul/li[3]/a"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 3
        "select_other_company":
            ("XPATH", "/html/body/div[2]/main/tz-partners/div/div[2]/div[5]/a"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 3
        "reference_other":
            ("XPATH", "/html/body/div[2]/main/tz-widget-market/div/div/div/div/div/a[4]"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 3
        "select_item_other":
            ("XPATH", "//tz-product-dialog-opener[starts-with(@name,'Tran')]"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 3
        "confirm_other_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button"),
        # General Sub-Menu Cart
        "cart_submenu":
            ("XPATH", "/html/body/header/tz-header-box/div/div/tz-cart-box/div[1]/div[1]"),
        # General Sub-Menu Checkout BTN
        "to_checkout":
            ("XPATH", "/html/body/header/tz-header-box/div/div/tz-cart-box/div[1]/div[2]/div/a"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 3
        "delete_checkout":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div[4]/div[1]"),
        # General Text Reference Main menu
        "reference_text":
            ("XPATH", "/html/body/div[2]/main/div/tz-widget-partners-list-carousel[1]/div/div[1]/div/h2"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 5
        "discover_btn":
            ("XPATH", "//*[@id='https://tazz.ro/cluj-napoca/restaurante']"),
        # General Filter Button
        "filter_btn":
            ("XPATH", "/html/body/div[2]/main/tz-partners-filters/div[1]/div/div[2]/tz-filters-dialog/div"),
        # General Filter Button
        "filter_by_delivery_checkbox":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[1]/div[1]/div[2]/div[10]"),
        # General Filter Button
        "filter_by_type_of_beverage":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[1]/div[2]/div[2]/div[4]"),
        # General Filter Button
        "filter_by_type_of_food":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[1]/div[2]/div[2]/div[9]"),
        # General Filter Button
        "apply_filters_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[2]/button"),
        # NOT_GENERAL (Preferred custom XPATH ) - Test 5
        "reference_filter_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[1]/div[2]/div[2]/div[27]"),
        # General Accept Cookies Button
        "accept_cookies_btn":
            ("XPATH", "/html/body/tz-cookie-consent/div/div[2]"),
        # General Badge content checkout
        "badge_reference":
            ("XPATH", "/html/body/header/tz-header-box/div/div/tz-cart-box/div[1]/div[1]/div[2]")

    }

    def input_restaurant_search(self):
        self.search_btn.click()
        time.sleep(1.765)
        self.search_btn.send_keys("Big Belly")
        time.sleep(1.765)
        self.select_big_belly_txt.click()
        time.sleep(1.765)

        # self.select_big_belly_btn.click()
        # Acest pas superior a fost scos deoarece site-ul "tazz.ro" a avut anumite update-uri la care utilizatorului
        # ii permit in mod direct sa acceseze restaurantul, fară să mai treaca printr-o fereastră de selecție a
        # restaurantelor cu nume similar

    def input_data_about_restaurant(self):

        # Folosit drept referinta pentru a face scroll pana la elementul dorit. Se poate lua drept referinta orice
        # alt element pentru care dorim sa facem actiunile

        time.sleep(2)
        # SCROLLING SCRIPT
        ref = self.reference_pizza
        coord = ref.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord['x'], coord['y']))
        time.sleep(3)
        # END OF SCROLLING SCRIPT

        self.choose_belly.click()
        time.sleep(1.765)

        ref2 = self.second_reference_pizza
        coord = ref2.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord['x'], coord['y']))
        time.sleep(3)

        self.choose_second_belly.click()
        time.sleep(1.765)
        self.select_final_both_btn.click()
        time.sleep(1.765)

        # Context menu stays open, so close it - General Method
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1.765)

        # Going back to intro page
        self.intro_page_btn.click()
        time.sleep(1.765)

    def other_acquisition(self):
        self.select_other_btn.click()
        time.sleep(1.765)
        self.select_other_company.click()
        time.sleep(1.765)

        # SCROLLING SCRIPT
        ref_2 = self.reference_other
        coord_2 = ref_2.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord_2['x'], coord_2['y']))
        time.sleep(3)
        # END OF SCROLLING SCRIPT

        self.reference_other.click()
        time.sleep(1.765)

        self.select_item_other.click()
        time.sleep(1.765)
        self.confirm_other_btn.click()
        time.sleep(1.765)

        if not self.badge_reference.is_displayed():
            if self.delete_checkout.is_displayed():
                self.delete_checkout.click()
                time.sleep(1.765)
            elif not (self.delete_checkout.is_displayed()):
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(1.765)

        sub_menu = self.cart_submenu
        actions = ActionChains(self.driver)
        actions.move_to_element(sub_menu).perform()
        time.sleep(1.765)

        self.to_checkout.click()
        time.sleep(1.765)

    def custom_search(self):
        # SCROLLING SCRIPT
        ref_3 = self.reference_text
        coord_3 = ref_3.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord_3['x'], coord_3['y']))
        time.sleep(3)
        # END OF SCROLLING SCRIPT

        self.discover_btn.click()
        time.sleep(1.765)

        # Applying the filters

        self.filter_btn.click()
        time.sleep(1.765)

        self.filter_by_delivery_checkbox.click()
        time.sleep(1.765)

        self.filter_by_type_of_beverage.click()
        time.sleep(1.765)

        self.filter_by_type_of_food.click()
        time.sleep(1.765)

        ref_4 = self.reference_filter_btn
        coord_4 = ref_4.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord_4['x'], coord_4['y']))
        time.sleep(3)

        self.accept_cookies_btn.click()
        time.sleep(1.765)

        self.apply_filters_btn.click()
        time.sleep(1.765)

        # END OF APPLYING FILTERS

# EOF
