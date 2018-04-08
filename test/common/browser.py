import time
import os
import sys
from selenium import webdriver
import sys
sys.path.append('E:\\Test_framework')
from tools.config import DRIVER_PATH, REPORT_PATH

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
FIREFOX_PATH = DRIVER_PATH + '\geckodriver.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {
    'firefox': webdriver.Firefox,
    'chrome': webdriver.Chrome,
    'ie': webdriver.Ie,
    'phantomjs': webdriver.phantomjs
}

EXECUTABLE_PATH = {
    'firefox': FIREFOX_PATH, 
    'chrome': CHROMEDRIVER_PATH, 
    'ie': IEDRIVER_PATH, 
    'phantomjs': PHANTOMJSDRIVER_PATH
}

class UnSupportBrowserTypeError(Exception):
    pass

def browser(browser_type='chrome'):
    _type = browser_type.lower()
    if _type in TYPES:
        browser = TYPES[_type]
    else:
        raise UnSupportBrowserTypeError('仅支持%s!'% ','.join(TYPES.keys()))

    driver = browser(executable_path=EXECUTABLE_PATH[_type])

    return driver
    
