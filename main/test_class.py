import logging

from pytest_check import equal

# noinspection PyUnresolvedReferences
from main.conftest import browser
from start_test import StartTest

logger = logging.getLogger()


class TestHomework:

    def test_homework(self, browser):
        logger.info('')
        homework_page = StartTest(browser) \
            .on_homework_page() \
            .log_in('dterepa@inbox.lv', 'Riga2021') \
            .fill_search('cool')
        search_text = homework_page.get_search_result_text()[0]
        homework_page.click_favourite_button() \
            .press_close_button() \
            .open_dropdown() \
            .open_favourites()
        favourites_text = homework_page.get_favourites_title_text()
        equal(search_text, favourites_text)
