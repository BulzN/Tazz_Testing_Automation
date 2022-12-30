# Tazz_Intro_Page.py - Prima Pagina de acum înainte, unde s-au salvat cookies despre utilizator
# Selectând restaurante și alte cazuri pentru a face test-case-uri.
# Cu trecerea timpului, acest modul .py va fi îmbunătățit, introducând mai multe funții abstracte/generale alături de
# diverși locatori unici de identificare


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
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "select_big_belly_txt":
            ("XPATH", "/html/body/header/tz-header-box/div/div[1]/tz-search-box/div[1]/div[3]/div[1]/div[1]"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "select_big_belly_btn":
            ("XPATH", "//*[@id='restaurants']/div/div/div[2]/div/div/div/div/div[2]"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "reference_pizza":
            ("XPATH", "//*[@id='subcategory-13005-product-133422']/div/div"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "choose_belly":
            ("XPATH", "//*[@id='subcategory-13005-product-133426']/div/div"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "second_reference_pizza":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[3]/div[1]/div[3]/div[8]/div[1]/label/span"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "choose_second_belly":
            ("XPATH",
             "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[3]/div[1]/div[3]/div[11]/div[1]/label"),
        # NOT_GENERAL ( Preferred custom XPATH ) - Test 1
        "select_final_both_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button")
    }

    def input_restaurant_search(self):
        self.search_btn.click()
        time.sleep(2)
        self.search_btn.send_keys("Big Belly")
        time.sleep(2)
        self.select_big_belly_txt.click()
        time.sleep(2)
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
        time.sleep(2)

        ref2 = self.second_reference_pizza
        coord = ref2.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord['x'], coord['y']))
        time.sleep(3)

        self.choose_second_belly.click()
        time.sleep(2)
        self.select_final_both_btn.click()
        time.sleep(2)
