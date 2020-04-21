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


def stackoverflow_multi_process():
    """Processo Principal. Aplica a unidade do processo para todos os Logins
    existentes no arquivo de credencial"""

    file_path = 'input/credenciais/credenciais.xlsx'
    status, credenciais = ldc.read_credentials_file(file_path)



    # configurações do driver
    driver = stackoverflow_config()




def stackoverflow_single_process():
    """Processo Unitário.."""

    # configurações do driver
    driver = stackoverflow_config()



def stackoverflow_config():
        # Configurações do webdriver
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

        # Resgatando diretório do chromedriver
        chrome_path = which("chromedriver")

        # Chamando webdriver
        driver = webdriver.Chrome(
            executable_path=chrome_path,
            desired_capabilities=capabilities
            )

        return driver


def stackoverflow_login(driver, username, password):
    """Stack Overflow LogIn"""



def stackoverflow_logout(driver):
    """Stack Overflow LogOut"""
