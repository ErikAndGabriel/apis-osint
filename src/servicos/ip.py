import requests 
import json 
from config.config_apis import APIS 
from config.config_app import APP 
from style.banners import Banner

class BuscarIp:
    def __init__(self, ip, arquivo):
        self.ip = ip 
        self.arquivo = arquivo 
        self.dados = None 

    def Buscar(self):
        api = APIS["api_ip"]
        url = api["url"].format(self.ip)
        print(Banner.banner_ip)
        resposta = requests.get(url, timeout=api["tempo"])
        if resposta.status_code == 200:
            dados = resposta.json()
            CAMPOS = {
                "status": dados["status"],
                "country": dados["country"],
                "countryCode": dados["countryCode"],
                "region": dados["region"],
                "regionName": dados["regionName"],
                "city": dados["city"],
                "zip": dados["zip"],
                "lat": dados["lat"],
                "lon": dados["lon"],
                "timezone": dados["timezone"],
                "isp": dados["isp"],
                "org": dados["org"],
                "as": dados["as"],
                "query": dados["query"]
            }

            for chave, valor in CAMPOS.items():
                if valor != "N/A":
                    print(f"{chave} : {valor}")
            self.dados = dados
            return self.dados

        else:
            print("\nholve um erro!!")
    
class SalvarIp(BuscarIp):
    def __init__(self, ip, arquivo):
        super().__init__(ip, arquivo)

    def SalvarIp(self):
        if self.dados is None:
            self.Buscar()

        if self.dados is not None:
            with open(f"{self.arquivo}", "w") as arq:
                json.dump(self.dados, arq, indent=4)
            print(f"\narquivo salvo em {self.arquivo}")
        else:
            print("\nNao a dados para salvar.")

