class VistaConsolaReservas:
    def mostrar_menu(self):
        print("\n" + "=" * 50)
        print("     ✈️  SISTEMA DE RESERVA DE VUELOS")
        print("=" * 50)
        print("  1. Ver vuelos disponibles")
        print("  2. Realizar una reserva")
        print("  3. Ver reservas realizadas")
        print("  4. Salir")
        print("=" * 50)
    
    def mostrar_vuelos(self, vuelos):
        print("\n📋 --- Vuelos Disponibles ---")
        if not vuelos:
            print("   No hay vuelos registrados.")
        else:
            for vuelo in vuelos:
                print(f"   • {vuelo}")
    
    def solicitar_datos_reserva(self):
        print("\n📝 --- Nueva Reserva ---")
        numero_vuelo = input("   Ingrese el número de vuelo: ").strip().upper()
        nombre = input("   Ingrese su nombre: ").strip()
        return numero_vuelo, nombre
    
    def mostrar_reservas(self, reservas):
        print("\n📂 --- Reservas Realizadas ---")
        if not reservas:
            print("   No hay reservas realizadas aún.")
        else:
            for i, reserva in enumerate(reservas, 1):
                print(f"   {i}. {reserva}")
    
    def mostrar_mensaje(self, mensaje):
        print(f"\n   {mensaje}")
    
    def solicitar_opcion(self):
        return input("\n   Seleccione una opción (1-4): ").strip()