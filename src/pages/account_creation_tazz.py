# account_creation_tazz.py - Modul .py care execută crearea unui cont. Deoarece acesta are nevoie și de un human
# verification, nu am putut să mai continui cu testul, acesta fiind un proces care nu poate fi automatizat

from selenium.webdriver import ActionChains
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver import Keys
import time


class AccountCreation(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "create_new_account_btn":
            ("XPATH", "/html/body/tz-dialog/div[1]/div/div[2]/div/tz-cart-auth-dialog/div/div/a"),
        "name_account":
            ("XPATH", "//*[@id='registration_form_full_name']"),
        "email_account":
            ("XPATH", "//*[@id='registration_form_email_address']"),
        "telephone_account":
            ("XPATH", "//*[@id='registration_form_phone_number']"),
        "password_account":
            ("XPATH", "//*[@id='registration_form_password']"),
        "accept_conditions_btn":
            ("XPATH", "//*[@id='registration_form_has_accepted_tc']"),
        "cnf_acc_creation_btn":
            ("XPATH", "//*[@id='registration_form_submit']"),
        "begin_human_verification_btn":
            ("XPATH", "//*[@id='amzn-captcha-verify-button']"),
        "next_chechout_step":
            ("XPATH", "/html/body/tz-cart/div/div/div[2]/div/a"),
        "begin_new_account_btn":
            ("XPATH", "/html/body/main/div/div[1]/a")
    }

    def checkout_step(self):
        self.next_chechout_step.click()
        time.sleep(1.765)
        self.create_new_account_btn.click()
        time.sleep(1.765)

    def human_verification(self):
        self.begin_human_verification_btn.click()
        time.sleep(1.765)


    # def introduce_data_account(self):
    #     self.begin_new_account_btn.click()
    #     time.sleep(1.765)
    #     self.name_account.set_text("John Smith")
    #     time.sleep(1.765)
    #     self.email_account.set_text("ledubeqe@cyclelove.cc")
    #     time.sleep(1.765)
    #     self.telephone_account.set_text("0774948611")
    #     time.sleep(1.765)
    #     self.password_account.set_text("justfy123$")
    #     time.sleep(1.765)
    #     self.accept_conditions_btn.click()
    #     time.sleep(1.765)
    #     self.cnf_acc_creation_btn.click()
    #     time.sleep(1.765)

