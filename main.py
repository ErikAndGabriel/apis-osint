from projeto.apis.cep import ApiCep, Salvar
from projeto.apis.ip import BuscarIp, SalvarIp
from projeto.apis.email import BusacarEmail
from projeto.banner import Banners
from colorama import Fore, init
import time 
import os 

init(autoreset=True)


def clear():
    os.system('clear')

def menu_cep():
    while True:
        try:
            clear()
            print(Banners.Banner_Ferramentas) 
            print("\n[1] Buscar")
            print("[2] Buscar e salvar")
            print("[3] Menu principal")
            escolha = int(input("\nMenu@Cep >> "))

            if escolha == 1:
                cep = input("o cep: ")
                usuario = ApiCep(cep, "")
                usuario.Buscar()
                input("[ENTER]")

            elif escolha == 2:
                cep = input("o cep: ")
                arquivo = input("nome do arquivo: ")
                usuario = Salvar(cep, arquivo)
                usuario.BuscarCep()
                usuario.Salvar()
                input("[ENTER]")

            elif escolha == 3:
                print(f"{Fore.RED} voltando para o menu principal!!!, em 5 segundos")
                time.sleep(5)
                break

            else:
                input("escolha invalida!![ENTER]")
                continue

        except ValueError:
            input("somente numeros!, [ENTER]")
            continue

def menu_ip():
    while True:
        try:
            clear()
            print(Banners.Banner_Ferramentas) 
            print("\n[1] Buscar")
            print("[2] Buscar e salvar")
            print("[3] Menu principal")
            escolha = int(input("\nMenu@Ip >> "))
            
            if escolha == 1:
                ip = input("o ip: ")
                usuario = BuscarIp(ip, "")
                usuario.Buscar()
                input("[ENTER]")

            elif escolha == 2:
                ip = input("o ip: ")
                arquivo = input("nome do arquivo: ")
                usuario = SalvarIp(ip, arquivo)
                usuario.Buscar()
                usuario.Salvar()
                input("[ENTER]")

            elif escolha == 3:
                print(f"{Fore.RED} voltando para o menu principal!!!, em 5 segundos")
                time.sleep(5)
                break
            else:
                input("escolha invalida!![ENTER]")
                continue

        except ValueError:
            input("somente numeros!, [ENTER]")
            continue


def Menu():
    while True:
        try:
            clear()
            print(Banners.Banner_menu)
            print("[1] Buscar ip")
            print("[2] Buscar email")
            print("[3] Buscar cep")
            print("[4] Buscar cnpj")
            print("[0] sair")
            escolha = int(input("\nOsint@Menu > > >  "))

            if escolha == 1:
                menu_ip()
            
            elif escolha == 3:
                menu_cep()

        except ValueError:
            print("somente numeros!")

if __name__ == "__main__":
    Menu()
            
