import requests 
import json
from colorama import Fore, init
from projeto.banner import Banners

init(autoreset=True)

class ApiCep:
    def __init__(self, cep, nome_arquivo):
        self.cep = cep 
        self.dados = None 
        self.nome_arquivo = nome_arquivo

    def BuscarCep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()

            print(Banners.Banner_cep)
            print(Fore.RED +  "=" * 30)
            print(f"{Fore.BLUE}cep : {dados['cep']}")
            print(f"{Fore.BLUE}logradouro : {dados['logradouro']}")
            print(f"{Fore.BLUE}complemento : {dados['complemento']}")
            print(f"{Fore.BLUE}unidade: {dados['unidade']}")
            print(f"{Fore.BLUE}bairro : {dados['bairro']}")
            print(f"{Fore.BLUE}localidade : {dados['localidade']}")
            print(f"{Fore.BLUE}uf : {dados['uf']}")
            print(f"{Fore.BLUE}estado : {dados['estado']}")
            print(f"{Fore.BLUE}regiao : {dados['regiao']}")
            print(f"{Fore.BLUE}ibge : {dados['ibge']}")
            print(f"{Fore.BLUE}gia : {dados['gia']}")
            print(f"{Fore.BLUE}ddd : {dados['ddd']}")
            print(f"{Fore.BLUE}siafi : {dados['siafi']}")
            print(Fore.RED + "=" * 30)
            self.dados = dados
            return self.dados

        else:
            print("Erro Api fora do ar, verifique sua internet!!")

class Salvar(ApiCep):
    def __init__(self, cep, nome_arquivo):
        super().__init__(cep, nome_arquivo)

    def Salvar(self):
        if self.dados:
            with open(f"{self.nome_arquivo}.json", "w") as arquivo:
                json.dump(self.dados, arquivo, indent=4)
            print(f"nome do arquivo > {self.nome_arquivo}.json")
