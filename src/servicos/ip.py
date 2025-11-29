import requests 
import json 
from config.config_apis import APIS 
from config.config_app import APP 
from style.banners import Banner
from colorama import Fore, init

init(autoreset=True)

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
                f"{Fore.RED}status": Fore.BLUE + dados["status"],
                f"{Fore.RED}country": Fore.BLUE + dados["country"],
                f"{Fore.RED}countryCode": Fore.BLUE + dados["countryCode"],
                f"{Fore.RED}region": Fore.BLUE + dados["region"],
                f"{Fore.RED}regionName": Fore.BLUE + dados["regionName"],
                f"{Fore.RED}city": Fore.BLUE + dados["city"],
                f"{Fore.RED}zip": Fore.BLUE + dados["zip"],
                f"{Fore.RED}lat": Fore.BLUE + str(dados["lat"]),
                f"{Fore.RED}lon": Fore.BLUE + str(dados["lon"]),
                f"{Fore.RED}timezone": Fore.BLUE + dados["timezone"],
                f"{Fore.RED}isp": Fore.BLUE + dados["isp"],
                f"{Fore.RED}org": Fore.BLUE + dados["org"],
                f"{Fore.RED}as": Fore.BLUE + dados["as"],
                f"{Fore.RED}query": Fore.BLUE + dados["query"]
            }

            for chave, valor in CAMPOS.items():
                if valor != "N/A":
                    print(f"{chave} : {valor}")
            self.dados = dados
            return self.dados

        else:
            print(f"\n{Fore.RED}holve um erro!!")
    
class SalvarIp(BuscarIp):
    def __init__(self, ip, arquivo):
        super().__init__(ip, arquivo)

    def Salvar(self):
        if self.dados is None:
            self.Buscar()

        if self.dados is not None:
            with open(f"{self.arquivo}", "w") as arq:
                json.dump(self.dados, arq, indent=4)
            print(f"\n{Fore.GREEN}arquivo salvo em {Fore.YELLOW}{self.arquivo}")
        else:
            print(f"\n{Fore.RED}Nao a dados para salvar.")
