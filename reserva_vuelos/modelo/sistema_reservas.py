from modelo.vuelo import Vuelo
from modelo.reserva import Reserva

class SistemaDeReservas:
    def __init__(self):
        self.vuelos = [
            Vuelo("AR101", "Buenos Aires", 5),
            Vuelo("AR202", "Córdoba", 3),
            Vuelo("AR303", "Mendoza", 2),
            Vuelo("AR404", "Bariloche", 0),
        ]
        self.reservas = []
    
    def obtener_vuelos(self):
        return self.vuelos
    
    def obtener_reservas(self):
        return self.reservas
    
    def buscar_vuelo(self, numero_vuelo):
        for vuelo in self.vuelos:
            if vuelo.numero_vuelo == numero_vuelo:
                return vuelo
        return None
    
    def realizar_reserva(self, numero_vuelo, nombre_pasajero):
        vuelo = self.buscar_vuelo(numero_vuelo)
        if vuelo is None:
            return False, f"❌ Error: No existe el vuelo '{numero_vuelo}'."
        if vuelo.asientos_disponibles <= 0:
            return False, f"❌ Error: No hay asientos en el vuelo {numero_vuelo}."
        if not nombre_pasajero:
            return False, "❌ Error: El nombre no puede estar vacío."
        
        nueva_reserva = Reserva(nombre_pasajero, vuelo)
        self.reservas.append(nueva_reserva)
        vuelo.asientos_disponibles -= 1
        return True, f"✅ ¡Reserva exitosa! {nombre_pasajero} → {vuelo.destino}."