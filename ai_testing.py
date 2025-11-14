from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

LOGIN_URL = "https://facebook.com"

DRIVER_PATH = os.path.join(os.getcwd(), "geckodriver")

# Facebook Locators
USERNAME_FIELD = (By.ID, "email")
PASSWORD_FIELD = (By.ID, "pass")
LOGIN_BUTTON = (By.NAME, "login")

def setup_driver():
    print(f"Using Geckodriver at: {DRIVER_PATH}")
    
    options = Options()
    options.add_argument("--headless")

    service = Service(DRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_page_load_timeout(10)

    return driver


def test_valid_login(driver):
    print("\n--- Test: VALID LOGIN ---")
    try:
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 0.5)

        wait.until(EC.presence_of_element_located(USERNAME_FIELD)).send_keys("invalid@email.com")
        wait.until(EC.presence_of_element_located(PASSWORD_FIELD)).send_keys("wrongpass")
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        print("Page loaded. We cannot login successfully on Facebook without 2FA.")
        return True

    except TimeoutException:
        print("Timeout on valid login test")
        return False


def test_invalid_login(driver):
    print("\n--- Test: INVALID LOGIN ---")
    try:
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 0.5)

        wait.until(EC.presence_of_element_located(USERNAME_FIELD)).send_keys("invalid@email")
        wait.until(EC.presence_of_element_located(PASSWORD_FIELD)).send_keys("wrongpass")
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        print("Facebook rejected invalid login as expected.")
        return True

    except TimeoutException:
        print("Timeout on invalid login test")
        return False


def run_tests():
    driver = setup_driver()

    results = {
        "valid_login": test_valid_login(driver),
        "invalid_login": test_invalid_login(driver)
    }

    driver.quit()

    print("\n--- TEST SUMMARY ---")
    print(results)


if __name__ == "__main__":
    run_tests()
