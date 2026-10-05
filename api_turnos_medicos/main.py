from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

# ---------------------------------------------------------
# INSTANCIA DE FASTAPI (Nuestro servidor web)
# ---------------------------------------------------------
app = FastAPI(
    title="Sistema de Gestión de Turnos Médicos",
    description="API REST para administrar médicos y sus turnos",
    version="1.0.0"
)

# ---------------------------------------------------------
# MODELOS DE PYDANTIC (Validación y Serialización JSON)
# Según la Clase 2: "La serialización convierte estructuras
# complejas en un formato plano (JSON) para transmitir por red"
# ---------------------------------------------------------
class MedicoBase(BaseModel):
    """Esquema base con los campos comunes de un médico."""
    nombre: str
    especialidad: str
    activo: bool = True
    dias_atencion: List[str]

class MedicoCreate(MedicoBase):
    """Esquema para CREAR un médico (lo que envía el cliente en el body)."""
    pass

class Medico(MedicoBase):
    """Esquema completo de un médico (incluye el id generado por el servidor)."""
    id: int

    class Config:
        from_attributes = True

# ---------------------------------------------------------
# BASE DE DATOS SIMULADA EN MEMORIA
# (En un proyecto real, aquí estaría la capa de datos/Persistencia)
# ---------------------------------------------------------
medicos_db: List[dict] = [
    {
        "id": 1,
        "nombre": "Dra. Ana Gómez",
        "especialidad": "Cardiología",
        "activo": True,
        "dias_atencion": ["Lunes", "Miércoles", "Viernes"]
    },
    {
        "id": 2,
        "nombre": "Dr. Carlos Pérez",
        "especialidad": "Pediatría",
        "activo": True,
        "dias_atencion": ["Martes", "Jueves"]
    }
]

# ---------------------------------------------------------
# ENDPOINTS RESTful (Mapeo de verbos HTTP a acciones)
# Según la Clase 2: "Los endpoints deben representar entidades,
# nunca acciones" → /medicos (sustantivo en plural) ✅
# ---------------------------------------------------------

# 🔹 GET /medicos → Listar todos los médicos
# Código de estado: 200 OK (petición exitosa)
@app.get("/medicos", response_model=List[Medico], status_code=status.HTTP_200_OK)
def obtener_medicos():
    """Retorna la lista completa de médicos registrados."""
    return medicos_db


# 🔹 GET /medicos/{id} → Obtener un médico específico
# Path Parameter: {id} forma parte de la URL para identificar el recurso
# Código de estado: 200 OK o 404 Not Found
@app.get("/medicos/{medico_id}", response_model=Medico, status_code=status.HTTP_200_OK)
def obtener_medico(medico_id: int):
    """Retorna el detalle de un médico específico según su ID."""
    medico = next((m for m in medicos_db if m["id"] == medico_id), None)
    
    if not medico:
        # 404: El recurso solicitado no existe
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Médico con ID {medico_id} no encontrado"
        )
    return medico


# 🔹 POST /medicos → Crear un nuevo médico
# Body Parameters: los datos viajan en el cuerpo de la petición (JSON)
# Código de estado: 201 Created (el recurso se creó exitosamente)
@app.post("/medicos", response_model=Medico, status_code=status.HTTP_201_CREATED)
def crear_medico(medico: MedicoCreate):
    """Registra un nuevo médico recibiendo los datos en formato JSON."""
    # Generar ID autoincremental simulado
    nuevo_id = max((m["id"] for m in medicos_db), default=0) + 1
    
    # Construir el nuevo médico (serialización inversa: JSON → objeto)
    nuevo_medico = {
        "id": nuevo_id,
        **medico.dict()  # Desempaqueta los campos del modelo Pydantic
    }
    
    medicos_db.append(nuevo_medico)
    return nuevo_medico


# 🔹 DELETE /medicos/{id} → Eliminar un médico
# Código de estado: 204 No Content (éxito pero sin cuerpo en la respuesta)
@app.delete("/medicos/{medico_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_medico(medico_id: int):
    """Elimina al médico correspondiente según su ID."""
    global medicos_db
    
    # Verificar que el médico exista antes de eliminarlo
    medico = next((m for m in medicos_db if m["id"] == medico_id), None)
    if not medico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Médico con ID {medico_id} no encontrado"
        )
    
    # Filtrar la lista eliminando al médico con ese ID
    medicos_db = [m for m in medicos_db if m["id"] != medico_id]
    return None