import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        # log in first
        user = "DarthVader"
        pwd = "Nebraska"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        # assert "Logged in"
        # find 'UserList' and click it – note this is all one Python statement
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()

        time.sleep(5)
        try:
            # verify User List exists on new screen after clicking "User List" button
            # attempt to find the 'User Detail' button - if found, the test viewed the correct pages
            elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/table/tbody/tr[1]/td[12]/a")

            assert True

        except NoSuchElementException:
            self.fail("User List page does not appear when User List is clicked")
            assert False

    time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()