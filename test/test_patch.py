#import requests

#def test_patch_users():

#    encabezado = {"x-api-key": "reqres-free-v1"}
#    url = "https://reqres.in/api/users/2"

#    data = {"name":"jose"}

#    response  = requests.patch(url,headers=encabezado,json=data)

#    assert response.status_code == 200
    
    
#    body = response.json()

#    assert body["name"] == data["name"]

#    assert "updatedAt" in body
#    assert isinstance(body["name"],str)
import requests

def test_patch_users(url_base):

    url = f"{url_base}/posts/1"

    data = {
        "name": "jose"
    }

    response = requests.patch(url, json=data)

    assert response.status_code == 200

    body = response.json()

    # Validaciones correctas para JSONPlaceholder
    assert body["name"] == data["name"]
    assert isinstance(body["name"], str)
    assert "id" in body

   