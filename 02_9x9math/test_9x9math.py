import os
import unittest
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Math9x9Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.button_id = {"plus": "button_plus",
                         "minus": "button_minus",
                         "times": "button_times",
                         "divide": "button_divide",
                         }
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['platformVersion'] = '6.0'
        cls.desired_caps['deviceName'] = 'Android Emulator'
        cls.desired_caps['app'] = PATH(
            './com.blogspot.rulesare.9x9math.apk'
        )
        cls.desired_caps['appPackage'] = 'com.blogspot.rulesare.a9x9math'
        cls.desired_caps['appActivity'] = '.MainActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                      cls.desired_caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.start_activity(self.desired_caps['appPackage'],
                                   self.desired_caps['appActivity'])

    def tearDown(self):
        pass

    def _enter_game_of(self, game_name):
        self._click_button(self.button_id[game_name])

    def _click_button(self, button_name):
        element_btn = self.driver.find_element_by_id(button_name)
        if element_btn:
            element_btn.click()

    def _retrieve_text_from(self, text_name):
        element = self.driver.find_element_by_id(text_name)
        return element.text

    def _retrieve_expression(self):
        """
        :return:  (operator, op1, op2)
        """
        inputA = self._retrieve_text_from("textA")
        inputB = self._retrieve_text_from("textB")
        inputOP = self._retrieve_text_from("textOperator")
        return (inputOP, inputA, inputB)

    def _calculate(self, op, value1, value2):
        if op == "+":
            return int(value1) + int(value2)
        elif op == "-":
            return int(value1) - int(value2)
        elif op == "*":
            return int(value1) * int(value2)
        elif op == "/":
            return int(value1) / int(value2)
        else:
            return 0

    def _click_button_with_answer(self, answer):
        for i in ("button1", "button2", "button3"):
            element = self.driver.find_element_by_id(i)
            if int(element.text) == answer:
                element.click()
                break

    def test_gaming_plus_1_run(self):
        self._enter_game_of("plus")
        op, v1, v2 = self._retrieve_expression()
        answer = self._calculate(op, v1, v2)
        self._click_button_with_answer(answer)

    def test_gaming_plus_10_run(self):
        self._enter_game_of("plus")
        for i in xrange(10):
            op, v1, v2 = self._retrieve_expression()
            answer = self._calculate(op, v1, v2)
            self._click_button_with_answer(answer)

    def test_gaming_minus_10_run(self):
        self._enter_game_of("minus")
        for i in xrange(10):
            op, v1, v2 = self._retrieve_expression()
            answer = self._calculate(op, v1, v2)
            self._click_button_with_answer(answer)

    def test_gaming_times_10_run(self):
        self._enter_game_of("times")
        for i in xrange(10):
            op, v1, v2 = self._retrieve_expression()
            answer = self._calculate(op, v1, v2)
            self._click_button_with_answer(answer)

    def test_gaming_divide_10_run(self):
        self._enter_game_of("divide")
        for i in xrange(10):
            op, v1, v2 = self._retrieve_expression()
            answer = self._calculate(op, v1, v2)
            self._click_button_with_answer(answer)


if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(Math9x9Tests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(verbosity=3)
