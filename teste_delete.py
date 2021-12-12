import requests

headers = {'Authorization': 'Token c6ad4a70d75b5fb0cc171c53596cb4168f18b15a'} # o token tem que ser de um super user para fazer o put

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}10/', headers=headers)

# Testando o codigo HTTP
assert resultado.status_code == 204

#print(resultado.text)

# Testando se o tamanho do conteudo retornado eh 0
assert len(resultado.text) == 0