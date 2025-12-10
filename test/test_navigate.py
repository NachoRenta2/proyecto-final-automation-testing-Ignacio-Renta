from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login(login_in_driver):
 try:    
    driver = login_in_driver
    assert '/inventory.html' in driver.current_url
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")#busco todos los elementos
    products[0].find_element(By.CSS_SELECTOR,".inventory_item button").click()#busco solo el primero
    count_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
    assert count_cart == "1", "No se a agregado producto"    

    print("test ok") 

 finally:
  
    driver.quit()