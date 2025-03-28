# Generated by Selenium IDE
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestVerifyallsearchesdone:
    def setup_method(self, method):
        options = Options()
        options.add_argument(f"user-data-dir={os.getenv('USER_DATA_DIR')}")
        options.add_argument(f"profile-directory={os.getenv('PROFILE_DIRECTORY')}")
        options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_verifyallsearchesdone(self):
        mobile_searches_done: bool = False
        desktop_searches_done: bool = False
        self.driver.get("https://rewards.bing.com/pointsbreakdown")
        search_desktop_goal: int = int(os.getenv("SEARCH_DESKTOP_GOAL"))
        search_mobile_goal: int = int(os.getenv("SEARCH_MOBILE_GOAL"))
        for _ in range(int(os.getenv("ATTEMPTS"))):
            if (
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    ".pointsBreakdownCard:nth-child(1) .pointsDetail .pointsDetail",
                ).text
                == f"{search_desktop_goal} / {search_desktop_goal}"
            ) is True:
                desktop_searches_done = True
            if (
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    ".pointsBreakdownCard:nth-child(2) .pointsDetail .pointsDetail",
                ).text
                == f"{search_mobile_goal} / {search_mobile_goal}"
            ) is True:
                mobile_searches_done = True
            if desktop_searches_done and mobile_searches_done:
                break
        assert desktop_searches_done, "Desktop searches not done"
        assert mobile_searches_done, "Mobile searches not done"
        self.driver.close()
