# LinuxRecon

**LinuxRecon** es una herramienta básica de auditoría para sistemas Linux orientada a automatizar la fase inicial de *Information Gathering* dentro de una evaluación de seguridad.

La aplicación recopila información relevante del sistema y la centraliza en un informe de texto para facilitar su revisión posterior.

## Funcionalidades

LinuxRecon obtiene:

- Información del sistema operativo y del kernel.
- Usuario que ejecuta la herramienta.
- UID, GID y grupos del usuario.
- Usuarios registrados en el sistema.
- Procesos en ejecución.
- Puertos TCP y UDP en escucha.
- Interfaces y configuración de red.
- Archivos con el bit SUID activo.

## Requisitos

- Sistema operativo Linux.
- Python 3.
- Comandos estándar: `uname`, `whoami`, `id`, `cut`, `ps`, `ss`, `ip` y `find`.

No requiere librerías externas de Python.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/TU-USUARIO/linuxrecon.git
cd linuxrecon
```

También puedes descargar el proyecto y acceder manualmente a la carpeta.

## Ejecución

```bash
python3 my.py
```

Selecciona la opción:

```text
1. Generar reporte completo
```

La herramienta creará el archivo:

```text
report.txt
```

Para revisar el informe:

```bash
less report.txt
```

## Estructura del proyecto

```text
linuxrecon/
├── my.py
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── examples/
│   └── report_example.txt
└── docs/
    └── screenshots/
        └── README.md
```

## Ejemplo de uso

```text
===================================
      LinuxRecon - TFM Tool
===================================
1. Generar reporte completo
2. Salir
Selecciona una opción: 1
[+] Generando reporte...
[+] Reporte generado correctamente: report.txt
```

## Consideraciones de seguridad

LinuxRecon está diseñada para utilizarse exclusivamente en sistemas propios o en entornos donde exista autorización expresa.

La aparición de un puerto abierto, un proceso o un archivo SUID no implica automáticamente la existencia de una vulnerabilidad. Los resultados requieren interpretación y análisis contextual por parte del profesional de seguridad.

Los informes generados pueden contener nombres de usuario, direcciones IP, interfaces de red y otros datos del sistema. No deben publicarse sin anonimizar previamente la información sensible.

## Limitaciones

- La herramienta realiza recopilación y no sustituye una auditoría profesional completa.
- Algunos resultados dependen de los privilegios del usuario que ejecuta el programa.
- Está orientada a distribuciones Linux con comandos compatibles.
- No realiza explotación ni modificación del sistema.

## Trabajo futuro

- Exportación a JSON y HTML.
- Clasificación automática de hallazgos.
- Integración con Nmap o Lynis.
- Generación de métricas y niveles de riesgo.
- Integración con plataformas SIEM.
- Interfaz gráfica o panel web.

## Autoría

Proyecto desarrollado por **Mirelle Candida Silva** como Trabajo Fin de Máster en Ciberseguridad.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE).
