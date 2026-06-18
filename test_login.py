import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature('Авторизация')
@allure.story('Успешный вход')
@allure.title('Проверка успешной авторизации с валидными данными')
@allure.description('Этот тест проверяет, что пользователь может войти в систему с правильным логином и паролем.')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(driver):
    with allure.step('Открыть страницу логина'):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step('Ввести логин и пароль'):
        username = driver.find_element(By.ID, "username")
        username.clear()
        username.send_keys("tomsmith")

        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("SuperSecretPassword!")

    with allure.step('Нажать кнопку Login'):
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    with allure.step('Проверить, что появилось сообщение об успехе'):
        wait = WebDriverWait(driver, 10)
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        assert "You logged into a secure area!" in success_message.text
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('Авторизация')
@allure.story('Неуспешный вход')
@allure.title('Проверка ошибки при входе с неверным паролем')
@allure.description('Этот тест проверяет, что система показывает сообщение об ошибке при вводе неверного пароля.')
@allure.severity(allure.severity_level.CRITICAL)
def test_unsuccessful_login(driver):
    with allure.step('Открыть страницу логина'):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step('Ввести логин и НЕВЕРНЫЙ пароль'):
        username = driver.find_element(By.ID, "username")
        username.clear()
        username.send_keys("tomsmith")

        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("WrongPassword123!")

    with allure.step('Нажать кнопку Login'):
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    with allure.step('Проверить, что появилось сообщение об ошибке'):
        wait = WebDriverWait(driver, 10)
        error_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )
        assert "Your password is invalid!" in error_message.text
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)