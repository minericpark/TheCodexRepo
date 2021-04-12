from selenium import webdriver
from selenium.webdriver.support.ui import Select
from AccountObj import AccountObj
from enum import Enum
import time


class FbAutomator:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com")
        self.driver.find_element_by_link_text("Create New Account").click()
        time.sleep(0.1)

        self.firstNameElem = self.driver.find_element_by_name("firstname")
        self.lastNameElem = self.driver.find_element_by_name("lastname")
        self.emailElem = self.driver.find_element_by_name("reg_email__")
        self.emailReElem = None
        self.passwordElem = self.driver.find_element_by_id("password_step_input")
        self.birthdayMonthElem = Select(self.driver.find_element_by_name("birthday_month"))
        self.birthdayDayElem = Select(self.driver.find_element_by_name("birthday_day"))
        self.birthdayYearElem = Select(self.driver.find_element_by_name("birthday_year"))
        self.genderSelectElem = self.driver.find_elements_by_name("sex")

    @staticmethod
    def create_account_obj(first_name, last_name, email, password, birth_month, birth_day, birth_year, gender):
        return AccountObj(first_name, last_name, email, password, birth_month, birth_day, birth_year, gender)

    def automate_create_call(self, account_obj):
        self.firstNameElem.send_keys(account_obj.first_name)
        self.lastNameElem.send_keys(account_obj.last_name)
        self.emailElem.send_keys(account_obj.email)
        time.sleep(0.1)
        self.emailReElem = self.driver.find_element_by_name("reg_email_confirmation__")
        self.emailReElem.send_keys(account_obj.email)
        self.passwordElem.send_keys(account_obj.password)
        self.birthdayMonthElem.select_by_visible_text(account_obj.birth_month)
        self.birthdayDayElem.select_by_visible_text(account_obj.birth_day)
        self.birthdayYearElem.select_by_visible_text(account_obj.birth_year)
        self.genderSelectElem[account_obj.gender].click()
        self.driver.find_element_by_link_text("Sign Up")

    def create_fb_account(self, first_name, last_name, email, password, birth_month, birth_day, birth_year, gender):
        account_obj = self.create_account_obj(first_name, last_name, email, password, birth_month, birth_day, birth_year,
                                              gender)
        self.automate_create_call(account_obj)
