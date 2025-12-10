from selenium.webdriver.common.by import By
import time
def login(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")#busca un elemento en una web con determinado ID
    driver.find_element(By.ID,"password").send_keys("secret_sauce")#ademas de buscar en este caso un campo, le establece valores
    driver.find_element(By.ID,"login-button").click()#hago click

    time.sleep(2)
    
    