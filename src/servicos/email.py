import os
from style.banner import Banner

class BuscarEmail:
    def __init__(self, email):
        self.email = email 

    def Buscar(self):
        print(Banner.banner_email)
        os.system(f'holehe {self.email}')
