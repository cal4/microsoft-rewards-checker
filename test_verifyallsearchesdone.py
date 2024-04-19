# Generated by Selenium IDE
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestVerifyallsearchesdone:
    def setup_method(self, method):
        options = Options()
        options.add_argument(
            "user-data-dir=C:\\Users\\cal\\AppData\\Local\\Google\\Chrome\\User Data"  # todo make configurable
        )
        options.add_argument("profile-directory=Profile 3")  # todo make configurable
        options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_verifyallsearchesdone(self):
        self.driver.get("https://rewards.bing.com/pointsbreakdown")
        search_desktop_goal: int = int(os.getenv("SEARCH_DESKTOP_GOAL"))
        assert (
            self.driver.find_element(
                By.CSS_SELECTOR,
                ".pointsBreakdownCard:nth-child(1) .pointsDetail .pointsDetail",
            ).text
            == f"{search_desktop_goal} / {search_desktop_goal}"
        )
        search_mobile_goal: int = int(os.getenv("SEARCH_MOBILE_GOAL"))
        assert (
            self.driver.find_element(
                By.CSS_SELECTOR,
                ".pointsBreakdownCard:nth-child(2) .pointsDetail .pointsDetail",
            ).text
            == f"{search_mobile_goal} / {search_mobile_goal}"
        )
        self.driver.close()
