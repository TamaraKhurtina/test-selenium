from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("SuperSecretPassword!")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))

    assert "You logged into a secure area!" in success_message.text

def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("111111111123!")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error")))

    assert "Your password is invalid!" in error_message.text