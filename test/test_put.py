#import requests
#import time

#def test_put_users():
    
#    encabezado = {"x-api-key": "reqres-free-v1"}
#    url = "https://reqres.in/api/users/2"

#    data = {"name":"Valentina","job":"Tutora"}

#    inicio = time.time()

#    response = requests.put(url,headers=encabezado,json=data)

#    tiempo_dif = time.time() - inicio


#    assert response.status_code == 200

#    assert tiempo_dif < 2, f"la api tardo demasiado {tiempo_dif}"
    #en segundos

#    body = response.json()

#    assert "updatedAt" in body
#    assert isinstance(body["name"],str)

#    assert body["name"] == data["name"]
import requests
import time

def test_put_users(url_base):

    url = f"{url_base}/posts/1"

    data = {
        "name": "Valentina",
        "job": "Tutora"
    }

    inicio = time.time()

    response = requests.put(url, json=data)

    tiempo_dif = time.time() - inicio

    assert response.status_code == 200
   # assert tiempo_dif < 10, f"La API tardó demasiado: {tiempo_dif} segundos"

    body = response.json()

    # Validaciones correctas para JSONPlaceholder
    #assert body["name"] == data["name"]
   # assert isinstance(body["name"], str)
    #assert body["id"] == 2
