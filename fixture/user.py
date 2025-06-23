from selenium.webdriver.support.ui import Select
from model.user import User
import re
class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        wd.find_element_by_link_text("home").click()
        self.user_cache = None

    def add_user_to_group(self, id, group):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group.name)
        wd.find_element_by_css_selector("input[name=\"add\"]").click()

    def delete_user_from_group(self, id, group):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text(group.name)
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text("group page \"Test\"").click()


    def edit_user_by_index(self, user, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        self.user_cache = None

    def edit_user_by_id(self, user, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_tag_name("a[href='edit.php?id=%s']" % id).click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
        self.user_cache = None

    def delete_first_user(self):
        wd = self.app.wd

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_link_text("home").click()
        self.user_cache = None

    def delete_user_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_link_text("home").click()
        self.user_cache = None

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.homephone)
        self.change_field_value("email", user.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_users_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.user_cache.append(User(firstname=firstname, lastname=lastname, id=id, address=address, all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails))
        return list(self.user_cache)

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_users_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return User(homephone=homephone, workphone=workphone,
                    mobilephone=mobilephone)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        id= wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        faxphone = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return User(id=id, firstname=firstname, lastname=lastname, address=address, homephone=homephone, workphone=workphone, mobilephone=mobilephone, faxphone=faxphone, email=email, email2=email2, email3=email3)

    def get_users_from_home_page(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        id = row.find_element_by_tag_name("input").get_attribute("value")
        firstname = row.find_elements_by_tag_name("td")[2].text
        lastname = row.find_elements_by_tag_name("td")[1].text
        address = row.find_elements_by_tag_name("td")[3].text
        return User(id=id, firstname=firstname, lastname=lastname, address=address)
