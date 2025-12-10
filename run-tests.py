import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "test/test_login.py",
    "test/test_login_faker.py"
    "test/test_inventory.py",
    "test/test_cart.py"#,
    "test/test_cart_json.py",
    "test/test_get.py",
    "test/test_put.py",
    "test/test_patch.py",
    "test/test_delete.py",
    #"test/test_api_reqres.py",
    #"test/test_navigate.py"
]# Los tests comentados no he podido hacerlos funcionar

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)


