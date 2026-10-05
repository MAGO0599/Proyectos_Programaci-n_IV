# 🏥 API REST - Sistema de Gestión de Turnos Médicos

**Materia:** Programación IV  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Instituto:** Instituto Tecnológico de Santiago del Estero (ITSE)  
**Año:** 2026

---

## 📝 Descripción

API REST desarrollada en **Python** utilizando el framework **FastAPI**, que permite gestionar médicos y sus turnos aplicando los principios de arquitectura **RESTful**, serialización **JSON** mediante **Pydantic** y los verbos HTTP correctos según los estándares del protocolo.

Este proyecto forma parte de la práctica de la Clase 2, donde se aplican los conceptos de:
- Protocolo HTTP (cliente-servidor)
- Verbos/Métodos HTTP (`GET`, `POST`, `DELETE`)
- Códigos de estado HTTP (`200`, `201`, `204`, `404`)
- Serialización y deserialización de datos en JSON
- Diseño de endpoints orientados a recursos

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Función |
|---|---|---|
| **Python** | 3.x | Lenguaje de programación backend |
| **FastAPI** | 0.142.x | Framework para construir APIs REST |
| **Pydantic** | 2.x | Validación y serialización de datos JSON |
| **Uvicorn** | 0.54.x | Servidor ASGI de alto rendimiento |

---

## 📁 Estructura del Proyecto

```
api_turnos_medicos/
│
├── main.py          ← Código principal de la API (endpoints, modelos, base de datos simulada)
└── README.md        ← Documentación del proyecto
```

---

## 🎯 Endpoints Implementados

La API expone los siguientes endpoints RESTful sobre el recurso `/medicos`:

| Método HTTP | Endpoint | Descripción | Código de Estado |
|---|---|---|---|
| `GET` | `/medicos` | Lista todos los médicos registrados | `200 OK` |
| `GET` | `/medicos/{id}` | Obtiene el detalle de un médico específico | `200 OK` / `404 Not Found` |
| `POST` | `/medicos` | Registra un nuevo médico (valida el JSON) | `201 Created` |
| `DELETE` | `/medicos/{id}` | Elimina un médico del sistema | `204 No Content` / `404 Not Found` |

---

## 📦 Modelo de Datos (Serialización JSON)

Cada médico se representa con la siguiente estructura:

```json
{
  "id": 1,
  "nombre": "Dra. Ana Gómez",
  "especialidad": "Cardiología",
  "activo": true,
  "dias_atencion": ["Lunes", "Miércoles", "Viernes"]
}
```

Los campos se validan automáticamente mediante modelos de **Pydantic**:

- `nombre` (string, obligatorio)
- `especialidad` (string, obligatorio)
- `activo` (booleano, por defecto `true`)
- `dias_atencion` (lista de strings, obligatorio)

---

## ⚙️ Requisitos Previos

- **Python 3.x** instalado en el sistema.
- Conexión a internet (solo para la instalación inicial de dependencias).

---

## 🚀 Instalación y Ejecución

### 1. Clonar o descargar el proyecto

```bash
cd C:\Users\Usuario\Desktop\Proyectos\api_turnos_medicos
```

### 2. Instalar las dependencias

```bash
pip install fastapi uvicorn
```

### 3. Iniciar el servidor de desarrollo

```bash
py -m uvicorn main:app --reload
```

El servidor se iniciará en:

👉 **http://127.0.0.1:8000**

> 💡 La opción `--reload` permite que el servidor se reinicie automáticamente al detectar cambios en el código.

---

## 🧪 Pruebas de los Endpoints

### 🔹 Listar todos los médicos (`GET /medicos`)

```bash
curl http://127.0.0.1:8000/medicos
```

**Respuesta esperada (200 OK):**
```json
[
  {
    "id": 1,
    "nombre": "Dra. Ana Gómez",
    "especialidad": "Cardiología",
    "activo": true,
    "dias_atencion": ["Lunes", "Miércoles", "Viernes"]
  },
  {
    "id": 2,
    "nombre": "Dr. Carlos Pérez",
    "especialidad": "Pediatría",
    "activo": true,
    "dias_atencion": ["Martes", "Jueves"]
  }
]
```

### 🔹 Obtener un médico específico (`GET /medicos/{id}`)

```bash
curl http://127.0.0.1:8000/medicos/1
```

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "nombre": "Dra. Ana Gómez",
  "especialidad": "Cardiología",
  "activo": true,
  "dias_atencion": ["Lunes", "Miércoles", "Viernes"]
}
```

**Si el médico no existe (404 Not Found):**
```json
{
  "detail": "Médico no encontrado"
}
```

### 🔹 Crear un nuevo médico (`POST /medicos`)

```bash
curl -X POST http://127.0.0.1:8000/medicos \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Dra. Laura Fernández",
    "especialidad": "Dermatología",
    "activo": true,
    "dias_atencion": ["Lunes", "Jueves"]
  }'
```

**Respuesta (201 Created):**
```json
{
  "id": 3,
  "nombre": "Dra. Laura Fernández",
  "especialidad": "Dermatología",
  "activo": true,
  "dias_atencion": ["Lunes", "Jueves"]
}
```

### 🔹 Eliminar un médico (`DELETE /medicos/{id}`)

```bash
curl -X DELETE http://127.0.0.1:8000/medicos/3
```

**Respuesta (204 No Content):** Sin cuerpo, solo el código de estado.

---

## 📖 Documentación Interactiva Automática

FastAPI genera automáticamente documentación interactiva para probar todos los endpoints:

- **Swagger UI:** 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Desde **Swagger UI** puedes:
- Visualizar todos los endpoints disponibles.
- Probar cada uno con el botón **"Try it out"**.
- Ver las respuestas con sus códigos de estado HTTP.

---

## 🎓 Conceptos Aplicados de la Clase 2

| Concepto | Aplicación en el proyecto |
|---|---|
| **Protocolo HTTP** | Comunicación cliente-servidor mediante peticiones y respuestas. |
| **Verbos HTTP** | Uso correcto de `GET`, `POST` y `DELETE` según la acción. |
| **Códigos de estado** | Respuestas con `200`, `201`, `204` y `404` según corresponda. |
| **Endpoints orientados a recursos** | Uso de sustantivos en plural (`/medicos`) en lugar de verbos. |
| **Serialización JSON** | Conversión automática de objetos Python a JSON mediante Pydantic. |
| **Validación de datos** | Los datos recibidos en el `body` se validan antes de procesarse. |
| **API RESTful** | Arquitectura basada en recursos, sin estado y con interfaz uniforme. |

---

## 👩‍💻 Autora

**Milagros**  
Tecnicatura Superior en Desarrollo de Software - ITSE  
Programación IV - 2026

---

## 📚 Referencias

- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Pydantic](https://docs.pydantic.dev/)
- [Material de Clase 2 - Programación IV (ITSE)](./Clase%202%20-%20ProgramaciónIV%20-%20ITSE.pptx)