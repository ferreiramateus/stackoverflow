"""
Project: Stack Overflow
Objective: Scraping the site stack overflow

Description:
This script was developed in order to navigate the site

https://stackoverflow.com/

Author: Mateus Ferreira
date: 2020/04/21
Python major version: 3.7
"""

import pandas as pd

from shutil import which
from datetime import date

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import common.utils as ldc


def stackoverflow_main():
    """Main Process"""

    # importing access credentials
    file_path = 'input/credentials.xlsx'
    status, credentials = ldc.read_credentials(file_path)

    # accessing credentials dictionary
    username = credentials.get('user')['stackoverflow']
    password = credentials.get('password')['stackoverflow']

    # chrome driver setup
    driver = stackoverflow_setup()

    # login step
    stackoverflow_login(driver, username, password)

    # navigate step
    stackoverflow_navigate(driver)



def stackoverflow_setup():
    # Webdriver Setup
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument(" --disable-gpu")
    options.add_argument(" --disable-infobars")
    options.add_argument(" -–disable-web-security")
    options.add_argument("--no-sandbox")
    options.add_argument("--DNS-prefetch-disable")
    capabilities = options.to_capabilities()

    # importing webdriver directory
    chrome_path = which("chromedriver")

    # calling webdriver
    driver = webdriver.Chrome(
        executable_path=chrome_path,
        desired_capabilities=capabilities
        )

    return driver


def stackoverflow_login(driver, username, password):
    """Stack Overflow LogIn"""

    # xpath dictionary used in this function
    xpath_dict = {
                    'user_element': '//*[@id="email"]',
                    'password_element': '//*[@id="password"]',
                    'login_element': '//*[@id="submit-button"]',
                   }

    tag = 'python'

    try:
        # webpage where the process starts
        driver.get(
            'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f'
            )

        # user field
        element_user = driver.find_element_by_xpath(
            xpath_dict.get('user_element')
            )
        element_user.click()
        element_user.send_keys(username)

        # password field
        element_password = driver.find_element_by_xpath(
            xpath_dict.get('password_element')
            )
        element_password.click()
        element_password.send_keys(password)

        # login button
        element_login = driver.find_element_by_xpath(
            xpath_dict.get('login_element')
            )
        element_login.click()

        print("User Login: ", username)


    except Exception as e:

        print('User:', username, ' Login Error: ', e)




def stackoverflow_navigate(driver):
    """Navigate through the stack overflow website"""

    # xpath dictionary used in this function
    xpath_dict = {
                      'tags_element': '//*[@id="nav-tags"]',
                      'tagfilter_element': '//*[@id="tagfilter"]',
                      'tagpython_element': '//*[@id="tags-browser"]/div[1]/div[1]/div/a'
                   }

    tag = 'python'

    try:

        # tag menu
        xpath_tuple = (By.XPATH, xpath_dict.get('tags_element'))
        xpath_visibility = EC.visibility_of_element_located(xpath_tuple)
        element_tags = WebDriverWait(driver, 5).until(xpath_visibility)
        element_tags.click()

        # tag filter field
        element_tagfilter = driver.find_element_by_xpath(
            xpath_dict.get('tagfilter_element')
            )
        element_tagfilter.click()
        element_tagfilter.send_keys(tag)
        element_tagfilter.send_keys(Keys.ENTER)

        # tag option
        tagpython_element = f'//*[@id="tags-browser"]/div[1]/div[1]/div/a[text()="{tag}"]'
        xpath_tuple = (By.XPATH, tagpython_element)
        xpath_visibility = EC.visibility_of_element_located(xpath_tuple)
        element_tags = WebDriverWait(driver, 5).until(xpath_visibility)
        element_tags.click()

    except Exception as e:
        print('Navigate Error: ', e)


def stackoverflow_logout(driver):
    """Stack Overflow LogOut"""
    pass
