import requests 
import json 
from style.banners import Banner
from config.config_apis import APIS 
from config.config_app import APP 

class BuscarCep:
    def __init__(self, cep, arquivo):
        self.cep = cep 
        self.arquivo = arquivo 
        self.dados = None

    def Buscar(self):
        api = APIS["api_cep"]
        url = api["url"].format(self.cep)

        resposta = requests.get(url, timeout=api["tempo"])
        print(Banner.banner_cep)

        if resposta.status_code == 200:
            dados = resposta.json()
            
            CAMPOS = {
                "cep": dados["cep"],
                "address_type": dados["address_type"],
                "address_name": dados["address_name"],
                "address": dados["address"],
                "state": dados["state"],
                "district": dados["district"],
                "lat": dados["lat"],
                "lng": dados["lng"],
                "city": dados["city"],
                "city_ibge": dados["city_ibge"],
                "ddd": dados["ddd"]
            }
            for chave, valor in CAMPOS.items():
                if valor != "N/A":
                    print(f"{chave} : {valor}")
            self.dados = dados
            return self.dados


class SalvarCep(BuscarCep):
    def __init__(self, cep, arquivo):
        super().__init__(cep, arquivo)
    def Salvar(self):
            if self.dados is None:
                self.Buscar()
            
            if self.dados is not None:
                with open(f"{self.arquivo}", "w") as arq:
                    json.dump(self.dados, arq, indent=4)
                print(f"arquivo Salvo em {self.arquivo}")
                return True
                
            else:
                print("nao tem dados para salvar")
                return False
