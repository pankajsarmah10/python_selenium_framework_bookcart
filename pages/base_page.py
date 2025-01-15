class BasePage:
    def __init__(self, driver=None):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title