from selenium.webdriver.support.events import AbstractEventListener

class WebDriverListener(AbstractEventListener):
    def __init__(self, logger):
        self.logger = logger

    def before_click(self, element, driver) -> None:
        self.logger.info(f"About to click on: {element.tag_name}")

    def after_click(self, element, driver) -> None:
        self.logger.info(f"Clicked on: {element.tag_name}")

    def before_navigate_to(self, url: str, driver) -> None:
        self.logger.info(f"About to navigate to: {url}")

    def after_navigate_to(self, url: str, driver) -> None:
        self.logger.info(f"Navigated to: {url} ")

    def on_exception(self, exception, driver) -> None:
        self.logger.error(f"Exception occurred: {exception} ")

