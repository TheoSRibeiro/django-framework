import requests

# GET Avaliacoes
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o codigo de status HTTP
print(avaliacoes.status_code)

# Acessando os dados da resposta
print(avaliacoes.json())

# Tipo de dado recebido
print(type(avaliacoes.json()))

# Acessando a quantidade de registros
print(avaliacoes.json()['count'])

# Acessando a proxima pagina de resultados
print(avaliacoes.json()['next'])

# Acessando os resultados desta pagina
print(avaliacoes.json()['results'])

# Tipo de dados da pagina
print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
print(avaliacoes.json()['results'][-1])

# Acessamdp o nome da pessoa que fez a ultima avaliacao
print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao
avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/3/')
print(avaliacao.json())

# GET cursos
cursos = requests.get('http://localhost:8000/api/v2/cursos/')
print('cursos_status code: ', cursos.status_code)
print('cursos: ', cursos.json())

headers = {'Authorization': 'Token 7d0bfe2e4d44f1f2871f0e9ac1b06c9f37ca2e4b'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print('cursos_status code: ', cursos.status_code)
print('cursos: ', cursos.json())