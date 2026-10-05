class Reserva:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo
    
    def __str__(self):
        return (f"Pasajero: {self.pasajero} | "
                f"Vuelo: {self.vuelo.numero_vuelo} "
                f"hacia {self.vuelo.destino}")