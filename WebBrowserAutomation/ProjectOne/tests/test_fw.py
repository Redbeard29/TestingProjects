import pytest

from pages.search import AmazonSearchPage
from pages.result import AmazonResultPage

def test_amazon_search(browser, phrase):

    search_page = AmazonSearchPage(browser)
    result_page = AmazonResultPage(browser)

    search_page.load()

    search_page.search(phrase)

    assert phrase == result_page.search_input_value()