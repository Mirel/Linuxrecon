# LinuxRecon

LinuxRecon is a lightweight Python tool developed as part of a Master's Final Project (TFM) in Cybersecurity. It automates local information gathering on Linux systems and centralizes the collected data in a structured text report.

## Scope

LinuxRecon collects information about the operating system, distribution, current user and groups, system users, user aliases, running processes, listening sockets, network interfaces and routes, mount points, disk usage, SUID files, recent system logs, and warning-level events.

The tool also produces an informational security summary. Detected SUID files, listening sockets, or warning events are **not automatically classified as vulnerabilities** and should be reviewed in context by an administrator or security analyst.

## Security improvements in the final version

- Commands are executed with argument lists rather than `shell=True`.
- Execution timeouts are applied to system commands.
- Common execution errors are handled explicitly.
- `/etc/os-release`, `/etc/passwd`, `.bashrc`, and `.bash_aliases` are read directly from Python where appropriate.
- The generated `report.txt` is protected with permissions `0600`.
- Recent logs and warning-level events are bounded to avoid unnecessarily large reports.

## Requirements

- Linux operating system
- Python 3
- Standard Linux utilities used by the tool (`uname`, `whoami`, `id`, `ps`, `ss`, `ip`, `findmnt`, `df`, `find`, `journalctl`)

No third-party Python packages are required.

## Usage

Clone or download the repository and run:

```bash
cd LinuxRecon
python3 src/my.py
```

Choose:

```text
1. Generar reporte completo
2. Salir
```

The report is generated as `report.txt` in the current working directory.

## Main report sections

- Información general del sistema
- Distribución y versión
- Usuario actual
- ID del usuario
- Usuarios del sistema
- Alias del usuario
- Procesos en ejecución
- Puertos abiertos
- Información de red
- Rutas de red
- Puntos de montaje
- Uso de sistemas de archivos
- Archivos con permisos SUID
- Logs recientes
- Warnings del sistema
- Resumen de seguridad

## Project structure

```text
LinuxRecon_GitHub_FINAL/
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   └── my.py
├── docs/
│   ├── TFM_LinuxRecon.pdf
│   ├── manual_usuario.md
│   └── metodologia_validacion.md
├── screenshots/
└── examples/
    └── report_example.txt
```

## Academic context

LinuxRecon was designed to demonstrate the automation, centralization, repeatability, and consistency of selected local information-gathering tasks in Linux. Its validation is functional and does not constitute a complete vulnerability assessment, CVE analysis, CVSS evaluation, exploitation framework, SIEM, or continuous monitoring solution.
