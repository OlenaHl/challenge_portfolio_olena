import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//div[1]/div[2]/span"
    players_xpath = "//div[2]/div[2]/span"
    sign_out_xpath = "//ul[2]/div[2]/div[2]/span"
    players_count_xpath = "//div[2]/div[1]/div/div[1]"
    matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    reports_count_xpath = "//div[2]/div[3]/div/div[1]"
    events_count_xpath = "//div[2]/div[4]/div/div[1]"
    dev_team_contact_xpath = "//div[3]/a/span[1]"
    shortcuts_xpath = "//div[2]/div/div/h2"
    add_player_xpath = "//a/button/span[1]"
    activity_xpath = "//div[3]/div/div/h2"
    last_created_player_xpath = "//div/div/h6[1]"
    test_name_test_surname_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//div[3]/div/div/h6[2]"
    tester_tester_xpath = "//a[2]/button/span[1]"
    last_updated_report_xpath = "//div[3]/div/div/h6[3]"
    test_testowy_xpath = "//a[3]/button/span[1]"
    scouts_panel_xpath = "//div[1]/div/div[2]/h2"
    polski_xpath = "//ul[2]/div[1]/div[2]/span"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title










