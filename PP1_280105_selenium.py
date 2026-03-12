import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginFormTests(unittest.TestCase):

    LOGIN_URL = "https://web.usos.pwr.edu.pl/kontroler.php?_action=logowaniecas/index"
    FIELD_NAME = "username"

    def setUp(self):
        # Używamy Safari, ale możesz zmienić na Chrome czy Firefox jeśli wolisz
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_enter_username(self):
        self.browser.get(self.LOGIN_URL)

        username_field = self.browser.find_element(By.NAME, self.FIELD_NAME)
        username_field.send_keys("user_test")

        current_value = username_field.get_attribute("value")
        self.assertEqual("user_test", current_value)

    def test_clear_username_field(self):
        self.browser.get(self.LOGIN_URL)

        username_field = self.browser.find_element(By.NAME, self.FIELD_NAME)
        username_field.send_keys("user_test")

        clear_btn = self.browser.find_element(By.NAME, "clear")
        clear_btn.click()

        cleared_value = username_field.get_attribute("value")
        self.assertEqual("", cleared_value)


if __name__ == "__main__":
    unittest.main()