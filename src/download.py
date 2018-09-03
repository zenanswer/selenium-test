#!/usr/bin/env python3

"""download.py: a simple demo for selenium."""

__copyright__   = "Copyright 2018, CIeNET Tech."


import traceback
import time

import setupdriver


if __name__ == '__main__':

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    chrome_options = webdriver.ChromeOptions()
    download_directory = {"download.default_directory": '.'}
    chrome_options.add_experimental_option("prefs", download_directory)

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.mozilla.org/zh-CN/firefox/new/?utm_medium=referral&utm_source=firefox-com")

        download_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-list"))
        )

        download_title.click()

        time.sleep(20)

    except Exception as exp:
        print(exp)
        traceback.print_exc()
    finally:
        driver.close()
