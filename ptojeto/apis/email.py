import json 
import os
from projeto.banner import Banners

class BusacarEmail:
    def __init__(self, email):
        self.email = email

    def Buscar(self):
        print(Banners.Banner_email)
        os.system(f'holehe {self.email}')
