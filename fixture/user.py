from model.user import User
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

    def edit_user_by_index(self, user, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
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

    def fill_user_form(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
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
            elements = wd.find_elements_by_css_selector("tr")
            for i in range(1, len(elements), 1):
                element = elements[i]
                xpath_id = i + 1
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = wd.find_element_by_xpath(f"//tr[{xpath_id}]/td[2]")
                firstname = wd.find_element_by_xpath(f"//tr[{xpath_id}]/td[3]")
                print (firstname.text)
                print(lastname.text)
                self.user_cache.append(User(firstname=firstname.text, lastname=lastname.text, id=id))
        return list(self.user_cache)

