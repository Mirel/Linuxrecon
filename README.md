# LinuxRecon

**LinuxRecon** es una herramienta de línea de comandos desarrollada en Python para automatizar y centralizar la fase inicial de **Information Gathering** en sistemas Linux.

Este proyecto forma parte de un **Trabajo Fin de Máster (TFM) en Ciberseguridad**. Su objetivo es recopilar de forma controlada información relevante del sistema y generar un informe estructurado denominado `report.txt`.

> **Importante:** LinuxRecon no es un escáner de vulnerabilidades. Recopila y organiza información para facilitar su posterior revisión por un administrador o analista de seguridad.

## Funcionalidades

LinuxRecon recopila información sobre:

- kernel, arquitectura y distribución Linux;
- usuario actual, UID, GID y grupos;
- usuarios registrados;
- alias del usuario;
- procesos en ejecución;
- puertos y sockets en escucha;
- interfaces y configuración de red;
- rutas de red;
- puntos de montaje;
- uso de los sistemas de archivos;
- archivos con permisos SUID;
- logs recientes;
- eventos de tipo warning.

También genera un **resumen informativo de seguridad** con elementos que pueden requerir una revisión posterior.

La presencia de un puerto abierto, un archivo SUID o un warning no implica automáticamente una vulnerabilidad.

## Seguridad

LinuxRecon utiliza `subprocess.run()` con listas de argumentos y sin `shell=True`.

La ejecución incorpora límites de tiempo (`timeout`), gestión de errores y tratamiento de comandos no disponibles.

El informe puede contener información sensible. Por este motivo, LinuxRecon aplica permisos `0600` a `report.txt`, limitando su lectura y modificación al propietario.

## Requisitos

- Python 3
- Sistema operativo GNU/Linux
- Utilidades nativas de Linux utilizadas por la herramienta

La versión del TFM fue desarrollada y validada principalmente en Ubuntu 25.04 ARM64/aarch64 mediante UTM.

## Instalación

```bash
git clone https://github.com/Mirel/Linuxrecon.git
cd Linuxrecon
python3 --version
```

## Ejecución

```bash
python3 src/my.py
```

La aplicación muestra:

```text
===================================
      LinuxRecon - TFM Tool
===================================
1. Generar reporte completo
2. Salir
```

Seleccionando la opción `1`, LinuxRecon genera `report.txt`.

Para consultar el informe:

```bash
less report.txt
```

Para comprobar sus permisos:

```bash
ls -l report.txt
```

El resultado esperado es equivalente a:

```text
-rw-------
```

## Estructura del repositorio

```text
Linuxrecon/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   └── my.py
├── docs/
│   ├── TFM_LinuxRecon.pdf
│   ├── manual_usuario.md
│   └── metodologia_validacion.md
└── screenshots/
    ├── permisos_suid.png
    ├── procesos.png
    ├── puertos_abiertos.png
    ├── report_1.png
    ├── report_2.png
    ├── rutas_red.png
    └── validacion_final.png
```

## Validación

Durante el TFM se realizaron pruebas funcionales para comprobar el funcionamiento de LinuxRecon y la consistencia de resultados seleccionados respecto a comandos nativos equivalentes.

La validación incluyó la ejecución de la aplicación, generación y regeneración de `report.txt`, recopilación de información del sistema, usuarios, procesos, puertos, red, rutas, sistemas de archivos, archivos SUID, logs, warnings, resumen de seguridad y protección del informe mediante permisos `0600`.

Las evidencias principales se encuentran en `screenshots/` y la metodología en `docs/metodologia_validacion.md`.

## Limitaciones

LinuxRecon es una herramienta de recopilación de información. No realiza identificación automática de CVE, valoración CVSS, explotación de vulnerabilidades, análisis remoto, monitorización continua ni correlación avanzada de eventos.

La interpretación de los resultados corresponde al analista.

La validación principal se realizó sobre Ubuntu 25.04 ARM64, por lo que el comportamiento en otras distribuciones y arquitecturas deberá comprobarse experimentalmente.

## Documentación

La carpeta `docs/` contiene:

- `TFM_LinuxRecon.pdf`: memoria del Trabajo Fin de Máster.
- `manual_usuario.md`: manual de utilización.
- `metodologia_validacion.md`: metodología y pruebas de validación.

## Líneas futuras

Entre las posibles ampliaciones se encuentran la validación en otras distribuciones y arquitecturas, modularización de la aplicación, sistema de plugins, exportación a JSON/HTML, nuevas comprobaciones e integración con otras herramientas de ciberseguridad.

## Uso responsable

LinuxRecon debe utilizarse únicamente sobre sistemas propios o sistemas para los que se disponga de autorización.

El proyecto tiene finalidad académica, educativa y de apoyo a tareas legítimas de administración y auditoría de seguridad.

## Autora

**Mirelle Candida Silva**

Trabajo Fin de Máster en Ciberseguridad.

## Licencia

Este repositorio no incluye actualmente una licencia de software.
