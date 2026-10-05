class Vuelo:
    def __init__(self, numero_vuelo, destino, asientos_disponibles):
        self.numero_vuelo = numero_vuelo
        self.destino = destino
        self.asientos_disponibles = asientos_disponibles
    
    def __str__(self):
        return (f"Vuelo {self.numero_vuelo} | "
                f"Destino: {self.destino} | "
                f"Asientos disponibles: {self.asientos_disponibles}")