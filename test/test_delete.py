#import requests
#import time

#def test_delete_users():
    
 #   encabezado = {"x-api-key": "reqres-free-v1"}
  #  url = "https://reqres.in/api/users/2"

    
   # response  = requests.delete(url,headers=encabezado)

    #assert response.status_code == 204
import requests

def test_delete_users(url_base):
    # Endpoint correcto en JSONPlaceholder
    url = f"{url_base}/posts/1"

    response = requests.delete(url)

    # JSONPlaceholder devuelve 200 en DELETE
    assert response.status_code == 200
