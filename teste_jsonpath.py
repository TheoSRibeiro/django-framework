import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
print(resultados)

primeiroElemento = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeiroElemento)

nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)
nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
print(nota)

curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
print(curso_id)

# Todos os nomes das pessoas que avaliaram o curso
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)

# Todos as avaliacoes das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)