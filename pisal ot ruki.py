From selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present (wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group (unittest.TestCase):
    def setUp (self):
        self.wd = WebDriver()
        self.wd.implicitly_wait (60)

    def test_test_add_group (self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.retturn_to_groups_page(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("logout").click()

    def retturn_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("bobbi")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("bobbi")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("bobbibobbi")
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input(type=\"submit\")").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()