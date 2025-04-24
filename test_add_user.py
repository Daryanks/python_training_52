# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from user import User
import unittest

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    def open_home_page(self, wb):
        wb.get("http://localhost/addressbook/")

    def login(self, wb, username, password):
        wb.find_element_by_name("user").click()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(username)
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()


    def add_new_user(self, wb, user):
        wb.find_element_by_link_text("add new").click()
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(user.firstname)
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(user.lastname)
        wb.find_element_by_name("company").click()
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(user.company)
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(user.address)
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(user.home)
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(user.email)
        wb.find_element_by_name("bday").click()
        Select(wb.find_element_by_name("bday")).select_by_visible_text(user.bday)
        wb.find_element_by_xpath("//option[@value='8']").click()
        wb.find_element_by_name("bmonth").click()
        Select(wb.find_element_by_name("bmonth")).select_by_visible_text(user.bmonth)
        wb.find_element_by_xpath("//option[@value='April']").click()
        wb.find_element_by_name("byear").click()
        wb.find_element_by_name("byear").send_keys(user.byear)
        wb.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    
    def test_add_user(self):
        wb = self.wb
        self.open_home_page(wb)
        self.login(wb, "admin", "secret")
        self.add_new_user(wb, User("First", "User", "Home", "N.Novgorod", "112", "u.first@mail.ru", "8", "2000", "April"))
        self.return_home_page(wb)
        self.logout(wb)

    def return_home_page(self, wb):
        wb.find_element_by_link_text("home").click()

    def logout(self, wb):
        wb.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wb.quit()
        

if __name__ == "__main__":

    unittest.main()
