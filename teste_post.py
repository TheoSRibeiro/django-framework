import requests

headers = {'Authorization': 'Token 7d0bfe2e4d44f1f2871f0e9ac1b06c9f37ca2e4b'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum2",
    "url": "http://geekuniversity.com.br/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HTTP 201 -- criado com sucesso
assert resultado.status_code == 201

# Testando se o titulo do curso retornado eh o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']