# Click Tracker 🖱️

Un sistema completo para capturar y registrar las coordenadas de clicks del mouse con logging avanzado y múltiples modos de ejecución.

## 📋 Características

-  ✅ **Captura de todos los clicks**: Detecta clicks izquierdo, derecho y medio
-  ✅ **Contador automático**: Lleva cuenta incremental de todos los clicks
-  ✅ **Logging dual**: Registra simultáneamente en archivo y consola
-  ✅ **Dos modos de ejecución**: Indefinido o con tiempo límite
-  ✅ **Archivos organizados**: Logs con timestamp en carpeta dedicada
-  ✅ **Manejo robusto de interrupciones**: Cierre limpio con Ctrl+C
-  ✅ **Arquitectura modular**: Código separado en componentes reutilizables

## 🏗️ Estructura del proyecto

```
click_tracker/
├── main.py              # Script principal con manejo de argumentos
├── click_tracker.py     # Clase del tracker de clicks
├── logger_config.py     # Configuración centralizada del logging
├── environment.yml      # Dependencias de conda
├── README.md           # Este archivo
└── logs/               # Carpeta generada automáticamente
    └── YYYYMMDD_HHMMSS.log
```

## 🚀 Instalación

### 1. Clonar o descargar los archivos

Asegúrate de tener todos los archivos Python en el mismo directorio.

### 2. Crear el environment de conda

```bash
conda env create -f environment.yml
```

### 3. Activar el environment

```bash
conda activate click_tracker
```

## 💻 Uso

### Modo Indefinido (por defecto)

Captura clicks hasta que presiones `Ctrl+C`:

```bash
python main.py
```

### Modo Temporal

Captura clicks por un tiempo específico:

```bash
# Capturar por 30 segundos
python main.py --seconds 30

# Capturar por 5 minutos
python main.py --seconds 300

# Capturar por 1 hora
python main.py --seconds 3600
```

### Ayuda

```bash
python main.py --help
```

## 📊 Ejemplo de output

### En consola:

```
=== CLICK TRACKER INICIADO (MODO TEMPORAL) ===
Duración: 30 segundos
El programa se detendrá automáticamente o presiona Ctrl+C
Todos los clicks serán registrados...
==================================================

2024-08-01 10:30:15 - ClickTracker - INFO - Click 1 coordenadas: [450, 300] - Botón: left
2024-08-01 10:30:16 - ClickTracker - INFO - Click 2 coordenadas: [520, 150] - Botón: right
2024-08-01 10:30:17 - ClickTracker - INFO - Click 3 coordenadas: [680, 400] - Botón: left

=== TIEMPO LÍMITE ALCANZADO ===

=== DETENIENDO CLICK TRACKER ===
Total de clicks registrados: 3
```

### En archivo de log (`logs/20240801_103014.log`):

```
2024-08-01 10:30:14 - ClickTracker - INFO - Logger configurado. Archivo de log: logs/20240801_103014.log
2024-08-01 10:30:14 - ClickTracker - INFO - === INICIANDO APLICACIÓN DE CAPTURA DE CLICKS ===
2024-08-01 10:30:14 - ClickTracker - INFO - Modo: Temporal (30 segundos)
2024-08-01 10:30:15 - ClickTracker - INFO - Iniciando captura de clicks por 30 segundos
2024-08-01 10:30:15 - ClickTracker - INFO - Timer iniciado para 30 segundos
2024-08-01 10:30:15 - ClickTracker - INFO - Click 1 coordenadas: [450, 300] - Botón: left
2024-08-01 10:30:16 - ClickTracker - INFO - Click 2 coordenadas: [520, 150] - Botón: right
2024-08-01 10:30:17 - ClickTracker - INFO - Click 3 coordenadas: [680, 400] - Botón: left
2024-08-01 10:30:44 - ClickTracker - INFO - Tiempo límite alcanzado - deteniendo captura
2024-08-01 10:30:44 - ClickTracker - INFO - Programa finalizado. Total de clicks registrados: 3
2024-08-01 10:30:44 - ClickTracker - INFO - === FINALIZANDO APLICACIÓN ===
```

## 🎯 Casos de uso

-  **Testing de aplicaciones**: Registrar patrones de interacción del usuario
-  **Análisis de UX**: Estudiar comportamientos de click en interfaces
-  **Automatización**: Capturar coordenadas para scripts de automatización
-  **Debugging**: Identificar problemas de usabilidad en aplicaciones
-  **Investigación**: Análisis de patrones de uso del mouse

## ⚙️ Configuración avanzada

### Personalizar el logger

Puedes modificar `logger_config.py` para cambiar:

-  Formato de los mensajes de log
-  Nivel de logging (DEBUG, INFO, WARNING, ERROR)
-  Ubicación de los archivos de log
-  Formato del timestamp en nombres de archivo

### Extender funcionalidades

La clase `ClickTracker` puede extenderse fácilmente para:

-  Filtrar tipos específicos de clicks
-  Agregar detección de double-clicks
-  Implementar zonas de exclusión
-  Añadir estadísticas en tiempo real

## 🛠️ Troubleshooting

### Error de permisos

En algunos sistemas, puede requerirse ejecutar con permisos especiales:

```bash
# En Linux/Mac
sudo python main.py

# En Windows (ejecutar como administrador)
```

### pynput no funciona

Si `pynput` no detecta eventos:

1. Verificar que el environment esté activado
2. Reinstalar pynput: `pip install --upgrade pynput`
3. En Linux, instalar dependencias del sistema: `sudo apt-get install python3-xlib`

### Logs no se crean

Verificar permisos de escritura en el directorio del proyecto.

## 📝 Notas técnicas

-  **Thread safety**: El programa usa threading para el timer pero mantiene thread-safety
-  **Signal handling**: Manejo robusto de `SIGINT` (Ctrl+C) en todos los modos
-  **Memory efficiency**: Almacena solo el contador, no historial completo de clicks
-  **Cross-platform**: Compatible con Windows, macOS y Linux

## 🤝 Contribuir

Para contribuir al proyecto:

1. Mantén la arquitectura modular existente
2. Añade logging apropiado para nuevas funcionalidades
3. Actualiza este README con cambios significativos
4. Prueba en diferentes sistemas operativos

## 📄 Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo según tus necesidades.

---

**¡Happy clicking!** 🖱️✨
