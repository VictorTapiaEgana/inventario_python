# Sistema de Inventario - Documentación Técnica

## Tabla de Contenidos
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modelos de Datos](#modelos-de-datos)
- [Guía de Configuración](#guía-de-configuración)
- [Arquitectura del Sistema](#arquitectura-del-sistema)

---

## Estructura del Proyecto

```
Inventario-Python/
├── .git/                    # Control de versiones Git
├── .gitignore              # Archivos ignorados por Git
├── datos/                  # Directorio de almacenamiento de datos
│   └── inventario.txt      # Archivo JSON con datos del inventario
├── funciones/              # Módulos de lógica de negocio
│   ├── crear_producto.py   # Función para crear nuevos productos
│   ├── eliminar_producto.py # Función para eliminar productos
│   ├── mostrar_inventario.py # Función para mostrar inventario
│   └── inventario.py      # Operaciones CRUD del inventario
├── ui/                     # Componentes de interfaz de usuario
│   └── ventana.py         # Función para renderizar ventanas
├── main.py                # Punto de entrada principal
└── DOCUMENTATION.md       # Este archivo de documentación
```

### Descripción de Directorios

- **`datos/`**: Contiene el archivo `inventario.txt` que almacena persistentemente los datos del inventario en formato JSON.
- **`funciones/`**: Módulos que implementan la lógica de negocio del sistema.
- **`ui/`**: Componentes responsables de la presentación visual y la interfaz de usuario.
- **`main.py`**: Archivo principal que orquesta el flujo de la aplicación.

---

### Flujo Detallado por Operación

#### 1. Crear Producto
```
Input Usuario → crear_producto.py → Validación de Datos → 
guardar_inventario() → JSON Write → datos/inventario.txt
```

#### 2. Eliminar Producto
```
Input Usuario → eliminar_producto.py → cargar_inventario() → 
JSON Read → Modificación en memoria → eiminar_por_id() → 
JSON Write → datos/inventario.txt
```

#### 3. Mostrar Inventario
```
Input Usuario → mostrar_inventario.py → cargar_inventario() → 
JSON Read → Formato Tabular → Presentación UI
```

### Transformación de Datos

1. **Entrada**: Datos validados del usuario (texto, números)
2. **Procesamiento**: Estructuración en diccionarios Python
3. **Almacenamiento**: Serialización JSON en archivo de texto
4. **Presentación**: Deserialización JSON → Formato tabular con `tabulate`

---

## Modelos de Datos

### Estructura de Producto

```python
{
    "nombre": str,        # Nombre del producto (máximo 25 caracteres)
    "descripcion": str,   # Descripción detallada (máximo 25 caracteres)
    "precio": int,        # Valor numérico en pesos
    "stock": int,         # Cantidad disponible (número entero)
    "id": int            # Identificador único (agregado dinámicamente)
}
```

### Estructura de Menú

```python
{
    "texto": str,         # Contenido a mostrar
    "align": str         # Alineación: "center" o "left"
}
```

### Tipos de Datos Principales

- **`list[dict[str, str | int]]`**: Estructura principal del inventario
- **`dict[str, str]`**: Configuración de elementos de menú
- **`bool`**: Estados de control de flujo
- **`None`**: Tipo de retorno para funciones sin valor de retorno

### Validaciones de Datos

- **Nombre**: No vacío, no numérico, no espacios en blanco
- **Stock**: Entero positivo mayor a cero
- **Precio**: Entero positivo mayor a cero  
- **Descripción**: No vacía, no numérica, no espacios en blanco
- **ID**: Entero positivo dentro del rango del inventario

---

## Guía de Configuración

### Dependencias del Sistema

#### Librerías Externas
```bash
pip install tabulate
```

#### Librerías Estándar Requeridas
- `json` - Para serialización/deserialización de datos
- `os` - Para limpieza de consola
- `typing` - Para anotaciones de tipo (Python 3.9+)

### Configuración de Archivos

#### Archivo de Datos
- **Ubicación**: `datos/inventario.txt`
- **Formato**: JSON con indentación de 4 espacios
- **Encoding**: UTF-8
- **Permisos**: Lectura/Escritura requeridos

### Instalación y Ejecución

1. **Clonar/Descargar el proyecto**
2. **Instalar dependencias**:
   ```bash
   pip install tabulate
   ```
3. **Ejecutar aplicación**:
   ```bash
   python main.py
   ```
---

## Arquitectura del Sistema

### Principios de Diseño

1. **Separación de Responsabilidades**: Cada módulo tiene una función específica
2. **Persistencia Simple**: JSON en archivo de texto para facilidad de uso
3. **Validación Robusta**: Entradas de usuario validadas antes del procesamiento
4. **Interfaz Consistente**: Sistema de ventanas unificado para toda la aplicación

### Patrones Implementados

- **MVC Implícito**: 
  - Model: `funciones/inventario.py`
  - View: `ui/ventana.py`
  - Controller: `main.py` y módulos de funciones