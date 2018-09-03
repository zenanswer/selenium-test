#!/usr/bin/env python3

"""simpleness.py: a simple demo for selenium."""

__copyright__   = "Copyright 2018, CIeNET Tech."


import traceback

import setupdriver


if __name__ == '__main__':

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    try:
        driver.get("https://www.baidu.com/")
        print(driver.title)
        assert "百度一下，你就知道" in driver.title
        elem = driver.find_element_by_name("wd")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "n"))
        )
        driver.find_element_by_class_name("index-logo-srcnew")
        driver.get_screenshot_as_file("baidu_pycon.png")
        result = driver.find_element_by_css_selector("div#1")
        print(result)
    except Exception as exp:
        print(exp)
        traceback.print_exc()
    finally:
        driver.close()
