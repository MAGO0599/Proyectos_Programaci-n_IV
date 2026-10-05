# Sistema de Reserva de Vuelos - Patrón MVC

**Materia:** Programación IV  
**Instituto:** Instituto Tecnológico de Santiago del Estero (ITSE)  

## Descripción
Aplicación de consola desarrollada en Python que gestiona un sistema de reserva de vuelos aplicando el patrón de arquitectura Modelo-Vista-Controlador (MVC).

## Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación.
- `modelo/`: Contiene las clases `Vuelo`, `Reserva` y `SistemaDeReservas` (lógica de negocio).
- `vista/`: Contiene la clase `VistaConsolaReservas` (interfaz de usuario).
- `controlador/`: Contiene la clase `ControladorReservas` (intermediario).

## Requisitos
- Python 3.x instalado en el sistema.

## Cómo ejecutar
1. Abrir una terminal o consola en la carpeta raíz del proyecto (`reserva_vuelos`).
2. Ejecutar el siguiente comando:
   ```bash
   python main.py
   # o en Windows: py main.py