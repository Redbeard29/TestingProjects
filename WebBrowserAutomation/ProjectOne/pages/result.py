from selenium.webdriver.common.by import By

class AmazonResultPage:

    SEARCH_INPUT = (By.ID, 'twotabssearchtextbox')

    def __init__(self, browser):
        self.browser = browser

    def search_input_value(self):
        search_input = self.browser.find_elements(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value