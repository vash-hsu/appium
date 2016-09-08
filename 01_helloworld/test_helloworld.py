import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HelloWorldTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.string4test = "@_@/ Hello World!"

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            './com.blogspot.rulesare.helloworld_radiobutton.apk'
        )
        desired_caps['appPackage'] = 'com.blogspot.rulesare.helloworld_radiobutton'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_string_and_make_uppercase(self):
        "FAST: type String, click UpperCase, get STRING back"
        # type Hello World string into [editText]
        element_txt = self.driver.find_element_by_id("editText")
        if element_txt:
            # clean
            element_txt.clear()
            # type new string
            element_txt.send_keys(self.string4test)
        # click [All Upper Case]
        element_btn_upper = self.driver.find_element_by_id("radioButton_upper")
        if element_btn_upper:
            element_btn_upper.click()
        # check result
        string_on_screen = element_txt.text
        expected_result = self.string4test.upper()
        self.assertEqual(string_on_screen, expected_result)

    def test_add_string_and_make_lowercase(self):
        "FAST: type String, click Lower, get string back"
        # type Hello World string into [editText]
        element_txt = self.driver.find_element_by_id("editText")
        if element_txt:
            # clean
            element_txt.clear()
            # type new string
            element_txt.send_keys(self.string4test)
        # click [All Upper Case]
        element_btn_upper = self.driver.find_element_by_id("radioButton_lower")
        if element_btn_upper:
            element_btn_upper.click()
        # check result
        string_on_screen = element_txt.text
        expected_result = self.string4test.lower()
        self.assertEqual(string_on_screen, expected_result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorldTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
