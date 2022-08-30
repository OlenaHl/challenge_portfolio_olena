import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//div[1]/div[2]/span"
    players_button_xpath = "//div[2]/div[2]/span"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_xpath = "//div[2]/div[1]/div/div[1]"
    matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    reports_count_xpath = "//div[2]/div[3]/div/div[1]"
    events_count_xpath = "//div[2]/div[4]/div/div[1]"
    dev_team_contact_xpath = "//div[3]/a/span[1]"
    shortcuts_xpath = "//div[2]/div/div/h2"
    add_player_button_xpath = "//*[text()='Add player']"
    activity_xpath = "//div[3]/div/div/h2"
    last_created_player_xpath = "//div/div/h6[1]"
    last_updated_player_xpath = "//div[3]/div/div/h6[2]"
    last_created_match_xpath = "//div[3]/div/div/h6[3]"
    scouts_panel_xpath = "//div[1]/div/div[2]/h2"
    polski_xpath = "//ul[2]/div[1]/div[2]/span"
    futbol_kolektyw_button_xpath = "//*[@title = 'Logo Scouts Panel']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_on_the_main_page_button(self):
        self.wait_for_visibility_of_element_located(self.main_page_button_xpath)
        self.click_on_the_element(self.main_page_button_xpath)










