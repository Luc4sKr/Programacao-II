"""

200 (OK): a solicitação ocorreu conforme o esperado e retornará algum dado, caso haja.
404 (NOT FOUND): não foi possível encontrar o endereço passado como parâmetro.
500 (INTERNAL SERVER ERROR): ocorreu algum erro no servidor.

"""

import requests

# URL da api
url = "https://rickandmortyapi.com/api/"

# resposta do request
response = requests.get(url)

# transforma em json
data = response.json()

print(data)
