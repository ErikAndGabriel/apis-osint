import requests 
import json 
from style.banners import Banner
from config.config_apis import APIS 
from config.config_app import APP 

class BuscarCnpj:
    def __init__(self, cnpj, arquivo):
        self.cnpj = cnpj 
        self.arquivo = arquivo
        self.dados = None 

    def Buscar(self):
        api = APIS["api_cnpj"]
        url = api["url"].format(self.cnpj)

        resposta 
