import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        #self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_header()
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        new_player = AddPlayer(self.driver)
        new_player.type_in_name('Adam')
        new_player.type_in_surname('Tomson')
        new_player.type_in_age('15.05.2000')
        new_player.type_in_main_position('front')
        new_player.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
