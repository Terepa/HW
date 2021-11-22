import homework_page as hp


class StartTest:

    def __init__(self, browser):
        self.browser = browser

    def on_homework_page(self):
        self.browser.get('https://newbuilds.com/')
        return hp.HomeworkPage(self.browser)
