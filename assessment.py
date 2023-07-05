import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_doodles_page():
    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    feeling_lucky_button = driver.find_element(By.NAME, "btnI")
    feeling_lucky_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.google.com/doodles"))

    current_url = driver.current_url

    assert current_url == "https://www.google.com/doodles"

    driver.quit()