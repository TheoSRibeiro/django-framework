import requests

class TestCursos:
    headers = {'Authorization': 'Token c6ad4a70d75b5fb0cc171c53596cb4168f18b15a'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers = self.headers)
        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programacao em Ruby 345",
            "url": "http://www.geekuniversity.com.br/cpr345"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):

        atualizacao = {
            "titulo": "Novo Curso de Ruby 4",
            "url": "http://geekuniversity.com.br/ncr4"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers, data=atualizacao)
        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizacao = {
            "titulo": "Novo Curso de Ruby 32",
            "url": "http://geekuniversity.com.br/ncr32"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers, data=atualizacao)
        assert resposta.json()['titulo'] == atualizacao['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url= f'{self.url_base_cursos}5/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0 # Nao retorna nenhum texto, somente e codigo 204

