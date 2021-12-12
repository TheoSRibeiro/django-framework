import requests

headers = {'Authorization': 'Token c6ad4a70d75b5fb0cc171c53596cb4168f18b15a'} # o token tem que ser de um super user para fazer o put

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://geekuniversity.com.br/ncs3"
}

# Buscando o curso com ID 11
curso = requests.get(url=f'{url_base_cursos}11/', headers=headers)
print(curso.json())

# f'' concatena os dados -> http://localhost:8000/api/v2/cursos/11/
resultado = requests.put(url=f'{url_base_cursos}11/', headers=headers, data=curso_atualizado)

# Testando o codigo de status HTTP
assert resultado.status_code == 200

# Testando o titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']