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
        cls.button_id = {"upper": "radioButton_upper",
                         "lower": "radioButton_lower"}
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['platformVersion'] = '6.0'
        cls.desired_caps['deviceName'] = 'Android Emulator'
        cls.desired_caps['app'] = PATH(
            './com.blogspot.rulesare.helloworld_radiobutton.apk'
        )
        cls.desired_caps['appPackage'] = 'com.blogspot.rulesare.helloworld_radiobutton'
        cls.desired_caps['appActivity'] = '.MainActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                      cls.desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # type Hello World string into [editText]
        self.element_txt = self.driver.find_element_by_id("editText")
        if self.element_txt:
            self.element_txt.clear() # clean
            self.element_txt.send_keys(self.string4test) # type new string

    def tearDown(self):
        pass

    def _click_button(self, button_name):
        element_btn = self.driver.find_element_by_id(button_name)
        if element_btn:
            element_btn.click()

    def _string_should_be(self, expected):
        string_on_screen = self.element_txt.text
        self.assertEqual(string_on_screen, expected)

    def test_add_string_and_make_uppercase(self):
        "FAST: type String, click UpperCase, get STRING back"
        self._click_button(self.button_id['upper']) # click [All Upper Case]
        self._string_should_be(self.string4test.upper()) # check result

    def test_add_string_and_make_lowercase(self):
        "FAST: type String, click Lower, get string back"
        self._click_button(self.button_id['lower']) # click [All Lower Case]
        self._string_should_be(self.string4test.lower()) # check result


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorldTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
