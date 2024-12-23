# test_login.py
import time
from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Case: Successful Login
def test_successful_login(driver):

    driver.find_element(By.XPATH, LoginLocator.login_link).click()
    driver.find_element(By.XPATH, LoginLocator.email_input).send_keys("test9909uer@gmail.com")
    driver.find_element(By.XPATH, LoginLocator.login_button).click()

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, LoginLocator.login_with_password)))
    time.sleep(3)
    driver.find_element(By.XPATH, LoginLocator.login_with_password).click()

    # Fill in the login credentials
    # time.sleep(5)

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, LoginLocator.email_id_login)))
    driver.find_element(By.XPATH, LoginLocator.email_id_login).send_keys("test9909user@gmail.com")
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, LoginLocator.password_login)))
    driver.find_element(By.XPATH, LoginLocator.password_login).send_keys("@test9909user@")

    # Submit the login form
    driver.find_element(By.XPATH, LoginLocator.submit_button).click()
    # time.sleep(2)

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, LoginLocator.loggedin_user)))
    # Check if login was successful
    username = driver.find_element(By.XPATH, LoginLocator.loggedin_user).text
    assert "Test" == username  # checking the logged-in username
    
    # Logout the user
    driver.find_element(By.XPATH, LoginLocator.loggedin_user).click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, LoginLocator.sign_out)))
    driver.find_element(By.XPATH, LoginLocator.sign_out).click()
    # time.sleep(2)

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, LoginLocator.login_link)))
    # Check if logout was successful
    button_text = driver.find_element(By.XPATH, LoginLocator.login_link).text
    assert "LOGIN" == button_text   
