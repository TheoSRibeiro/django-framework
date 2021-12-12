import requests

headers = {'Authorization': 'Token 7d0bfe2e4d44f1f2871f0e9ac1b06c9f37ca2e4b'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())
print(resultado.status_code)

# Testando se o endpoint esta correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 6

# Testando se o titulo do primeiro curso esta correto
assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'