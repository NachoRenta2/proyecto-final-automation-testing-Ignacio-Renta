#import requests

#def test_get_users(url_base):
 #   url = "https://reqres.in/api/users?page=2"#f"{url_base}/2" #leagrego parte a la url base el /2
  #  encabezado = {"x-api-key": "reqres-free-v1"}

   # response = requests.get(url,headers=encabezado)

    #assert response.status_code == 200

    #assert "data" in data

    #assert len(data["data"]) > 0
import requests

def test_get_users(url_base):
    # Endpoint correcto en JSONPlaceholder
    url = f"{url_base}/users"

    response = requests.get(url)

    # Validaciones
    assert response.status_code == 200

    data = response.json()

    # JSONPlaceholder devuelve una LISTA de usuarios
    assert isinstance(data, list)
    assert len(data) > 0