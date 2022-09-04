import unittest

from unittest.loader import makeSuite

from test_case.framework import Test
from test_case.login_to_the_system import TestLoginPage
from test_case.test_add_player import TestAddPlayer
from test_case.main_page import TestMainPage
from test_case.players_page import TestPlayers
from test_case.sign_out import TestSignOut
from test_case.remind_password import TestRemindPassword



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestMainPage))
   test_suite.addTest(makeSuite(TestPlayers))
   test_suite.addTest(makeSuite(TestSignOut))
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestRemindPassword))

   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())