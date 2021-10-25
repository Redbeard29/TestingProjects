from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class AmazonSearchPage:

    URL = 'https://www.amazon.com'

    SEARCH_DROPDOWN = (By.ID, 'searchDropdownBox')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def filter(self):
        search_category = Select(self.browser.find_element(*self.SEARCH_DROPDOWN))
        search_category.select_by_visible_text('Books')

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
