from pages.base_page import BasePage


class AddPlayer(BasePage):
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    age_xpath = "//input[@name='age']"
    main_position_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//*[text()='Submit']"


    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)


