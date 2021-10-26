from selenium.webdriver.common.by import By

class AmazonResultPage:

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    def __init__(self, browser):
        self.browser = browser

    def search_input_value(self):
        search_input = self.browser.find_elements(*self.SEARCH_INPUT)
        #SEARCH_INPUT is returning a list, we want the first item
        value = search_input[0].get_attribute('value')
        return value