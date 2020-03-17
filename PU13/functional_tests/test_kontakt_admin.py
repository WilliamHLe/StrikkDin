import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from django.urls import reverse

# These are the tests for interface. Please download requirements.txt one more time to include last package needed for these tests.

class TestContaktAdmin(StaticLiveServerTestCase):
    #this runs before all code
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver")
    #This runs after all the code
    def tearDown(self):
        self.browser.close()

    def test_kontakt_page(self):
        # The user request the kontakt admin page
        self.browser.get(self.live_server_url + "/kontakt")
        alert = self.browser.find_element_by_class_name("container")

        self.assertEquals(
            alert.find_element_by_tag_name("h2").text, "Send melding til admin"
        )


    def test_navigate_to_home_page(self):
        # The user try to navigate to the home-page
        self.browser.get(self.live_server_url + reverse("kontakt"))
        alert = self.browser.find_element_by_class_name("navbar")
        alert.find_element_by_tag_name("a").click()
        self.assertEquals(self.browser.current_url, self.live_server_url + "/")
        time.sleep(1)
