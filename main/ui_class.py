from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class UI:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)

    def open_page(self, url):
        if url.startswith('http://') or url.startswith('https://'):
            self.browser.get(url)
        else:
            self.browser.get('https://' + url)

    def wait_until_present(self, locator):
        self.wait.until(
            ec.presence_of_all_elements_located(locator))

    def wait_to_be_clickable(self, locator):
        self.wait.until(
            ec.element_to_be_clickable(locator))

    def get_element(self, locator):
        assert len(self.get_elements(locator)) != 0, 'No elements found'
        return self.get_elements(locator)[0]

    def get_elements(self, locator):
        self.wait_until_present(locator)
        return self.browser.find_elements(locator[0], locator[1])

    def clear_field(self, locator):
        self.wait_until_present(locator)
        self.get_element(locator).clear()
        return self

    def get_text(self, locator):
        return self.get_element(locator).text

    def get_text_from_web_element(self, web_element):
        return web_element.text, self

    def click(self, locator):
        self.wait_to_be_clickable(locator)
        self.get_element(locator).click()

    def click_by_number(self, locator, number):
        self.wait_until_present(locator)
        self.get_elements(locator)[number].click()

    def set_text(self, locator, text):
        self.clear_field(locator)
        self.get_element(locator).send_keys(text)

    def get_text_of_all_elements(self, locator):
        text = []
        for el in self.get_elements(locator):
            text.append(
                self.get_text_from_web_element(el)[0])
        return text
