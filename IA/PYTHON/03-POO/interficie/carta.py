from enviable import Enviar
from digital import Digital

class Carta(Enviar, Digital):
    
    def __init__(self, destinatari: str, digital: bool, missatge: str):
        # no hi ha super perquè només fer referència a uns comportaments, no un constructor
        self.missatge=missatge
        self.destinatari=destinatari
        self.digi=digital
        
    def enviar(self):
        #! inisteixo no cal super perquè no hem definit res
        return f"{self.destinatari}"
    
    def digital(self):
        if self.digi:
            return "Missatge digital"
        else:
            return "Missatge no digital"
    
    # la classe filla és on definirem aquest mètode
    def __str__(self):
        return f"Destinatari: {self.enviar()}, plataforma: {self.digital()}, missatge: {self.missatge}"