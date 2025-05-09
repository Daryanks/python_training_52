
class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        wd.find_element_by_link_text("home").click()

    def edit_first_user(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_user_form(user)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()

    def delete_first_user(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_link_text("home").click()

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

