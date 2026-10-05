# 💼 Portafolio Profesional con Bootstrap 5

**Materia:** Programación IV  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Instituto:** Instituto Tecnológico de Santiago del Estero (ITSE)  
**Año:** 2026

---

## 📝 Descripción

Este proyecto consiste en el desarrollo de una página web de portafolio personal, moderna y totalmente responsiva (adaptable a móviles, tablets y escritorio). Fue construida aplicando los fundamentos de **Bootstrap 5**, utilizando su sistema de cuadrícula (Grid), componentes prediseñados y clases de utilidad.

El sitio incluye las secciones clásicas de un portafolio profesional: navegación fija, hero de presentación, sección "Acerca de Mí" con imagen de perfil real, galería de proyectos en tarjetas interactivas, formulario de contacto con validación y pie de página con redes sociales.

## 🛠️ Tecnologías Utilizadas

| Tecnología | Función |
|---|---|
| **HTML5** | Estructura semántica del documento |
| **CSS3** | Estilos personalizados complementarios |
| **Bootstrap 5.3** | Framework CSS para diseño responsivo y componentes |
| **Bootstrap Icons** | Iconos de redes sociales en el footer |
| **Google Fonts** | Tipografía moderna (Poppins) |

## 📁 Estructura del Proyecto

```text
portafolio_bootstrap/
│
├── index.html          ← Archivo principal con la estructura y componentes de Bootstrap
├── css/
│   └── style.css       ← Estilos personalizados (tipografía, efectos hover, scroll suave)
├── img/
│   └── perfil_1.jpg    ← Imagen de perfil personal (usado en la sección "Acerca de Mí")
└── README.md           ← Documentación del proyecto
```

## 🎯 Requisitos del Ejercicio Cumplidos

Según la consigna de la **Clase 3 - Bootstrap (ITSE)**, el portafolio incluye todas las secciones solicitadas:

| Sección | Componente Bootstrap utilizado |
|---|---|
| **1. Barra de Navegación** | `navbar`, `navbar-expand-lg`, `fixed-top`, menú hamburguesa responsivo |
| **2. Sección Hero** | `container`, `text-center`, `display-4`, `btn`, `btn-lg` |
| **3. Acerca de Mí** | Sistema de grilla `row` + `col-md-5` / `col-md-7`, imagen `rounded-circle` |
| **4. Proyectos** | Grid responsivo `col-12` / `col-md-6` / `col-lg-4` con componentes `card` |
| **5. Contacto** | Formularios con `form-control`, `form-label`, `mb-3`, `d-grid` |
| **6. Footer** | `bg-dark`, `text-white`, iconos de Bootstrap Icons |

## 🚀 Cómo visualizar el proyecto

1. Descarga o clona la carpeta `portafolio_bootstrap` en tu computadora.
2. Abre el archivo `index.html` con cualquier navegador web moderno (Chrome, Edge, Firefox).
3. **No requiere servidor**: al ser HTML/CSS/JS estático, funciona con doble clic.

## 📱 Prueba de Responsividad

Para comprobar que el diseño se adapta correctamente a diferentes dispositivos:

1. Abre `index.html` en tu navegador.
2. Presiona **F12** para abrir las herramientas de desarrollo.
3. Haz clic en el ícono de **Device Toolbar** (Ctrl + Shift + M).
4. Prueba los siguientes dispositivos:
   - **Móvil** (< 576px): Menú hamburguesa, 1 columna de proyectos.
   - **Tablet** (768px - 992px): 2 columnas de proyectos, imagen y texto lado a lado.
   - **Escritorio** (> 992px): 3 columnas de proyectos, menú completo visible.

## 💡 Características Destacadas

- ✅ **Diseño 100% responsivo** gracias al sistema de grilla de Bootstrap 5.
- ✅ **Tipografía moderna** con Google Fonts (Poppins).
- ✅ **Efectos hover** en las tarjetas de proyectos (elevación y sombra al pasar el mouse).
- ✅ **Scroll suave** al hacer clic en los enlaces del menú.
- ✅ **Imagen de perfil real** en lugar de placeholders genéricos.
- ✅ **Separación de responsabilidades**: HTML, CSS y recursos en carpetas independientes.
- ✅ **Iconos profesionales** de Bootstrap Icons en el footer.

## 📚 Conceptos de Bootstrap Aplicados

| Concepto | Aplicación en el proyecto |
|---|---|
| **Container** | Uso de `.container` para delimitar y centrar el contenido. |
| **Grid System** | Sistema de 12 columnas con breakpoints `col-12`, `col-md-6`, `col-lg-4`. |
| **Navbar** | Barra de navegación fija con menú colapsable en móviles. |
| **Cards** | Tarjetas para mostrar los proyectos con imagen, título y descripción. |
| **Forms** | Formulario de contacto estilizado con clases de Bootstrap. |
| **Utilities** | Clases de utilidad como `text-center`, `py-5`, `mb-3`, `shadow-sm`, `fw-bold`. |
| **Images** | Imagen de perfil con `rounded-circle` y `img-fluid`. |

---

*Desarrollado como parte de la práctica de la Clase 3 de Programación IV - ITSE 2026.*