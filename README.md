# LinuxRecon

LinuxRecon es una herramienta ligera de **Information Gathering para sistemas Linux**, desarrollada como parte de un Trabajo Fin de Máster en Ciberseguridad.

Su objetivo es automatizar la recopilación inicial de información del sistema y centralizar los resultados en un informe de texto, evitando ejecutar manualmente múltiples comandos durante una primera fase de reconocimiento local.

## Funcionalidades

LinuxRecon recopila actualmente:

- Información general del sistema y arquitectura (`uname -a`).
- Usuario actual (`whoami`).
- UID, GID y grupos (`id`).
- Usuarios registrados en `/etc/passwd`.
- Procesos activos (`ps aux`).
- Puertos y sockets en escucha (`ss -tuln`).
- Interfaces y direcciones de red (`ip a`).
- Archivos con permisos SUID (`find / -perm -4000`).
- Generación automática de un informe `report.txt`.

## Requisitos

- Linux.
- Python 3.
- Utilidades estándar empleadas por el script: `uname`, `whoami`, `id`, `cut`, `ps`, `ss`, `ip` y `find`.

No requiere paquetes Python externos.

## Instalación

Clona el repositorio y entra en el directorio:

```bash
git clone https://github.com/Mirel/Linuxrecon.git
cd Linuxrecon
```

No es necesario instalar dependencias adicionales de Python.

## Uso

Ejecuta:

```bash
python3 my.py
```

La aplicación mostrará el menú:

```text
===================================
      LinuxRecon - TFM Tool
===================================
1. Generar reporte completo
2. Salir
```

Selecciona `1` para generar el informe. El resultado se guarda como:

```text
report.txt
```

> `report.txt` puede contener nombres de usuario, procesos, interfaces, direcciones IP y otra información del equipo. Por este motivo está excluido del repositorio mediante `.gitignore`.

## Estructura del repositorio

```text
LinuxRecon/
├── my.py
├── README.md
├── .gitignore
├── requirements.txt
├── SECURITY.md
├── CHANGELOG.md
├── CITATION.cff
├── docs/
│   ├── ARCHITECTURE.md
│   └── USAGE.md
└── examples/
    └── report_example.txt
```

## Arquitectura

La versión actual mantiene una arquitectura funcional sencilla:

```text
Usuario
  ↓
main()
  ↓
generate_report()
  ↓
Funciones de recopilación
  ↓
run_command()
  ↓
Sistema Linux
  ↓
report.txt
```

Las funciones de recopilación están separadas lógicamente para facilitar el mantenimiento y una futura evolución hacia módulos o plugins.

Consulta [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) para más información.

## Alcance

LinuxRecon es una herramienta de recopilación de información. **No es un escáner de vulnerabilidades** y no pretende sustituir herramientas profesionales como Lynis, OpenVAS, Nessus o plataformas SIEM.

La presencia de un puerto abierto, una cuenta o un archivo SUID no implica por sí misma una vulnerabilidad. Los resultados deben ser interpretados posteriormente por un analista.

## Seguridad y uso responsable

Utiliza LinuxRecon únicamente sobre sistemas propios o sobre aquellos para los que dispongas de autorización. La versión actual utiliza comandos predefinidos y está orientada principalmente a operaciones de consulta.

Consulta [`SECURITY.md`](SECURITY.md) para conocer las consideraciones de seguridad y las mejoras previstas.

## Evolución prevista

Entre las posibles ampliaciones se encuentran módulos para SSH, firewall, SGID, tareas cron, servicios, paquetes, actualizaciones, Docker y logs, además de exportación JSON/HTML y una futura arquitectura de plugins.

## Proyecto académico

LinuxRecon ha sido desarrollado como prototipo académico dentro de un Trabajo Fin de Máster en Ciberseguridad. El repositorio contiene el código fuente necesario para reproducir la versión utilizada durante la validación del proyecto.

## Licencia

Este repositorio no incluye actualmente una licencia de software. Antes de reutilizar, modificar o redistribuir el código, consulta las condiciones establecidas por la autora del proyecto.
