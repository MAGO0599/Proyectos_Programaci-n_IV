class ControladorReservas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.solicitar_opcion()
            
            if opcion == "1":
                self._ver_vuelos()
            elif opcion == "2":
                self._reservar_vuelo()
            elif opcion == "3":
                self._ver_reservas()
            elif opcion == "4":
                self.vista.mostrar_mensaje("👋 ¡Gracias por usar el sistema! Adiós.")
                break
            else:
                self.vista.mostrar_mensaje("⚠️  Opción inválida.")
    
    def _ver_vuelos(self):
        vuelos = self.modelo.obtener_vuelos()
        self.vista.mostrar_vuelos(vuelos)
    
    def _reservar_vuelo(self):
        numero_vuelo, nombre = self.vista.solicitar_datos_reserva()
        exito, mensaje = self.modelo.realizar_reserva(numero_vuelo, nombre)
        self.vista.mostrar_mensaje(mensaje)
    
    def _ver_reservas(self):
        reservas = self.modelo.obtener_reservas()
        self.vista.mostrar_reservas(reservas)