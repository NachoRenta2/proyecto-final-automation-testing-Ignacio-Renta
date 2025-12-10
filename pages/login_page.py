from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage:

    #URL
    URL = "https://www.saucedemo.com"

    _USER_INPUT = (By.ID,"user-name")
    _PASS_INPUT = (By.ID,"password")
    _LOGIN_BUTTON = (By.ID,"login-button")

    def __init__(self,driver): #self dentro de una clase, es como llamar a una funcion dentro de la misma clase
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def completar_user(self,usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT)) 
        input.clear()   
        input.send_keys(usuario)
        return self
    
    def completar_pass(self,password):
        input = self.driver.find_element(*self._PASS_INPUT)#significa que desempaqueta informacion, recepcion de multiples argumentos
        #input = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))  
        input.clear() 
        input.send_keys(password)
        return self
    
    def click_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self
    
    def login_completo(self,usuario,password):
        self.completar_user(usuario)
        self.completar_pass(password)
        time.sleep (1)
        self.click_button()
        return self

    def obtener_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3")))
        return div_error.text
# si quiero probar login incorrecto tendria que hacer otra funcion y ver los errores
        #este archivo reemplazaria el utils