from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.webdriver_listener import WebDriverListener
from selenium.webdriver.support.events import EventFiringWebDriver

class DriverFactory:

    def __init__(self, browser="chrome", headless=True, logger = None):
        self.browser = browser.lower()
        self.headless = headless
        self.logger = logger
    def get_driver(self):
        if self.browser == 'chrome':
            driver = self._get_chrome_driver()
        elif self.browser == 'firefox':
            driver = self._get_firefox_driver()
        else:
            raise ValueError(f"Browser {self.browser} is not supported")

        listener = WebDriverListener(self.logger)
        return EventFiringWebDriver(driver, listener)

    def _get_chrome_driver(self):
        chrome_options = ChromeOptions()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _get_firefox_driver(self):
        firefox_options = FirefoxOptions()
        if self.headless:
            firefox_options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=firefox_options)
