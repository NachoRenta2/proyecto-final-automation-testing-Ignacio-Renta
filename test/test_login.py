from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from dato import leer_csv_login
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario, password, debe_funcionar",(
("standard_user","secret_sauce",True), 
("admin","1234", False)
))
def test_login_validation(login_in_driver, usuario, password,debe_funcionar):
   
  driver = login_in_driver
      # driver
    #print(debe_funcionar)
    
  if debe_funcionar == 'True':
    assert "/inventory.html" in driver.current_url, "No se redirigio"
  elif debe_funcionar == 'False':
    mensaje_error = LoginPage(driver).obtener_error()
    assert "Epic sadface" in mensaje_error, "el mensaje no se esta mostrando"