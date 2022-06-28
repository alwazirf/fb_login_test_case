from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://facebook.com')
    yield driver
    driver.quit()


def test_login_true(driver):

    driver.find_element(By.ID, "email").send_keys('bagusbali003@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Bismillah123#' + Keys.ENTER)


def test_login_pass_false(driver):
    driver.find_element(By.ID, "email").send_keys('bagusbali003@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('xxxxxx' + Keys.ENTER)


def test_login_email_false(driver):
    driver.find_element(By.ID, "email").send_keys('xxxxxx@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Bismillah123#' + Keys.ENTER)


def test_login_passEmail_false(driver):
    driver.find_element(By.ID, "email").send_keys('xxxxxx@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('xxxxx' + Keys.ENTER)
