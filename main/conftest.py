import platform

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    os_name = platform.system()
    driver = None
    if os_name == 'Linux':
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['platform'] = "LINUX"
        driver = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor='35.204.124.126:4444/wd/hub')
    elif os_name == 'Darwin' or os_name == 'Windows':
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
    else:
        AssertionError(os_name + ' platform is not supported')
    driver.maximize_window()
    driver.set_page_load_timeout(15)
    yield driver
    driver.quit()
