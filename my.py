#!/usr/bin/env python3
"""
LinuxRecon
Herramienta básica de recopilación automatizada de información
para sistemas Linux.

Proyecto desarrollado como Trabajo Fin de Máster en Ciberseguridad.
"""

import subprocess
from datetime import datetime
from pathlib import Path


REPORT_FILE = Path("report.txt")


def run_command(command: str) -> str:
    """
    Ejecuta un comando del sistema y devuelve su salida estándar.

    Se utiliza subprocess.run para conservar los resultados incluso cuando
    el comando termina con un código distinto de cero, como puede ocurrir
    al buscar archivos SUID sin permisos de acceso a determinados directorios.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        if result.stdout.strip():
            return result.stdout

        if result.stderr.strip():
            return f"Advertencia: {result.stderr}"

        return "Sin resultados.\n"

    except Exception as exc:
        return f"Error ejecutando comando: {exc}\n"


def get_system_info() -> str:
    return run_command("uname -a")


def get_current_user() -> str:
    return run_command("whoami")


def get_user_id() -> str:
    return run_command("id")


def get_all_users() -> str:
    return run_command("cut -d: -f1 /etc/passwd")


def get_processes() -> str:
    return run_command("ps aux")


def get_open_ports() -> str:
    return run_command("ss -tuln")


def get_network_info() -> str:
    return run_command("ip a")


def get_suid_files() -> str:
    return run_command("find / -perm -4000 2>/dev/null")


def generate_report() -> None:
    """Genera un informe de texto con la información recopilada."""
    print("[+] Generando reporte...")

    report = f"""
=================================================
            LinuxRecon Security Report
=================================================
Fecha: {datetime.now()}

[INFORMACION DEL SISTEMA]
{get_system_info()}

[USUARIO ACTUAL]
{get_current_user()}

[ID DEL USUARIO]
{get_user_id()}

[USUARIOS DEL SISTEMA]
{get_all_users()}

[PROCESOS EN EJECUCION]
{get_processes()}

[PUERTOS ABIERTOS]
{get_open_ports()}

[INFORMACION DE RED]
{get_network_info()}

[ARCHIVOS CON PERMISOS SUID]
{get_suid_files()}

=================================================
Fin del reporte
=================================================
"""

    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"[+] Reporte generado correctamente: {REPORT_FILE}")


def main() -> None:
    """Muestra el menú principal de la herramienta."""
    print("===================================")
    print("      LinuxRecon - TFM Tool")
    print("===================================")
    print("1. Generar reporte completo")
    print("2. Salir")

    option = input("Selecciona una opción: ").strip()

    if option == "1":
        generate_report()
    elif option == "2":
        print("Saliendo...")
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
