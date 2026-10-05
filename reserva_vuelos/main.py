"""
Punto de entrada de la aplicación.
Aquí se ensamblan las tres capas del patrón MVC.
"""
from modelo import SistemaDeReservas
from vista import VistaConsolaReservas
from controlador import ControladorReservas


def main():
    # 1. Instanciar las tres capas
    modelo = SistemaDeReservas()
    vista = VistaConsolaReservas()
    controlador = ControladorReservas(modelo, vista)
    
    # 2. Iniciar la aplicación
    print("\n🚀 Iniciando Sistema de Reservas...")
    controlador.ejecutar()


if __name__ == "__main__":
    main()