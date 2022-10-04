import requests

from Acesso_CEP import BuscaEndereco

exemplo_cep = "01153000"
objeto_cep = BuscaEndereco(exemplo_cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print("CEP: {} - Bairro: {} - Cidade: {} - UF: {}".format(objeto_cep, bairro, cidade, uf))