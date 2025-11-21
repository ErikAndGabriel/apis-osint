from colorama import Fore, init 
from projeto.banner import Banners
import requests 
import json 

init(autoreset=True)

class BuscarIp:
    def __init__(self, ip, nome_arquivo):
        self.ip = ip 
        self.nome_arquivo = nome_arquivo
        self.dados = None

    def Buscar(self):
        url = f"https://ipinfo.io/{self.ip}/json"

        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            print(Banners.Banner_ip)
            print("=" * 30)
            print(f"ip : {dados['ip']}")
            print(f"hostname : {dados['hostname']}")
            print(f"city : {dados['city']}")
            print(f"region : {dados['region']}")
            print(f"country : {dados['country']}")
            print(f"loc : {dados['loc']}")
            print(f"org : {dados['org']}")
            print(f"postal : {dados['postal']}")
            print(f"timezone : {dados['timezone']}")
            print(f"readme : {dados['readme']}")
            print(f"anycast : {dados['anycast']}")
            print("=" * 30)
            self.dados = dados
            return self.dados

class SalvarIp(BuscarIp):
    def __init__(self, ip, nome_arquivo):
        super().__init__(ip, nome_arquivo)
    
    def Salvar(self):
        with open(f"{self.nome_arquivo}.json", "w") as arquivo:
            json.dump(self.dados, arquivo, indent=4)
