import time

from ui_class import UI
from selenium.webdriver.common.by import By


class HomeworkPage:
    LOG_IN_BUTTON = (By.XPATH,
                     ".//div[@class = 'hidden lg:flex space-x-8']/a[2]")
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'user[email]']")
    CONTINUE_BUTTON = (By.XPATH,
                       ".//button[@data-testid= 'modal-register-submit']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type = 'password']")
    BLUE_LOG_IN_BUTTON = (By.XPATH,
                          ".//button[@data-testid = 'modal-login-submit']")
    SEARCH_INPUT = (By.XPATH, ".//input[@name = 'filters[query]']")
    SEARCH_RESULT_INFORMATION = (By.XPATH,
                                 ".//div[@id = 'projects-search-result']//p")
    FAVOURITE_BUTTON = (By.XPATH,
                        ".//div[@id = 'projects-search-result']//button")
    CLOSE_BUTTON = (By.XPATH, ".//p[@class= 'hidden md:block']")
    DROPDOWN = (By.XPATH,
                ".//div[@class = 'hidden lg:inline-flex px-2 mx-auto']")
    MY_FAVOURITES = (
        By.XPATH, ".//div[@class = 'profile-menu__links "
                  "flex flex-col space-y-6']/a[3]")
    MY_FAVOURITES_TITLE = (
        By.XPATH, ".//div[@class = 'property-title truncate']")


    def __init__(self, browser):
        self.browser = browser
        self.ui = UI(browser)

    def log_in(self, email, password):
        self.ui.click(self.LOG_IN_BUTTON)
        self.ui.set_text(self.EMAIL_INPUT, email)
        self.ui.click(self.CONTINUE_BUTTON)
        time.sleep(0.5)
        self.ui.set_text(self.PASSWORD_INPUT, password)
        self.ui.click(self.BLUE_LOG_IN_BUTTON)
        return self

    def fill_search(self, item_to_search):
        time.sleep(1)
        self.ui.set_text(self.SEARCH_INPUT, item_to_search)
        return self

    def get_search_result_text(self):
        time.sleep(1)
        return self.ui.get_text_of_all_elements(self.SEARCH_RESULT_INFORMATION)

    def press_close_button(self):
        time.sleep(1)
        self.ui.click(self.CLOSE_BUTTON)
        return self

    def get_favourites_title_text(self):
        time.sleep(1)
        return self.ui.get_text(self.MY_FAVOURITES_TITLE)

    def open_dropdown(self):
        time.sleep(1)
        self.ui.click(self.DROPDOWN)
        return self

    def open_favourites(self):
        time.sleep(1)
        self.ui.click(self.MY_FAVOURITES)
        return self

    def click_favourite_button(self):
        time.sleep(1)
        self.ui.click_by_number(self.FAVOURITE_BUTTON, 1)
        return self
