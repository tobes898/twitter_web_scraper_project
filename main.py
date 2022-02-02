import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

# web driver instance
driver = Chrome()

# go to Twitter login page
driver.get('https://www.twitter.com/login')