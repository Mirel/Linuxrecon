import subprocess
from datetime import datetime
from pathlib import Path


# ============================================================
# Configuración
# ============================================================

REPORT_FILE = Path("report.txt")
COMMAND_TIMEOUT = 20


# ============================================================
# Ejecución segura de comandos
# ============================================================

def run_command(command, timeout=COMMAND_TIMEOUT):
    """
    Ejecuta comandos del sistema de forma controlada.

    Los comandos se proporcionan como listas de argumentos.
    No se utiliza shell=True, reduciendo el riesgo de
    inyección de comandos.

    Args:
        command (list[str]): comando y argumentos.
        timeout (int): tiempo máximo de ejecución.

    Returns:
        str: salida del comando o información del error.
    """

    if not isinstance(command, list) or not command:
        return "Error: formato de comando no válido.\n"

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        # Si existe salida válida, se devuelve aunque el comando
        # también haya producido advertencias en stderr.
        if stdout:
            return result.stdout

        if stderr:
            return (
                f"Advertencia al ejecutar {' '.join(command)}:\n"
                f"{result.stderr}"
            )

        if result.returncode != 0:
            return (
                f"El comando {' '.join(command)} finalizó "
                f"con código {result.returncode}.\n"
            )

        return "Sin resultados.\n"

    except FileNotFoundError:
        return (
            f"Error: no se encontró el comando "
            f"'{command[0]}'.\n"
        )

    except subprocess.TimeoutExpired:
        return (
            f"Error: el comando {' '.join(command)} "
            f"superó el tiempo máximo de {timeout} segundos.\n"
        )

    except Exception as e:
        return f"Error ejecutando comando: {e}\n"


# ============================================================
# Información del sistema
# ============================================================

def get_system_info():
    return run_command(["uname", "-a"])


def get_distribution_info():
    """
    Obtiene información de la distribución directamente
    desde /etc/os-release, evitando un subproceso innecesario.
    """

    os_release = Path("/etc/os-release")

    try:
        if os_release.exists():
            return os_release.read_text(encoding="utf-8")

        return "No se encontró /etc/os-release.\n"

    except OSError as e:
        return f"Error leyendo /etc/os-release: {e}\n"


# ============================================================
# Información de usuarios
# ============================================================

def get_current_user():
    return run_command(["whoami"])


def get_user_id():
    return run_command(["id"])


def get_all_users():
    try:
        with open("/etc/passwd", "r", encoding="utf-8") as passwd_file:
            users = [
                line.split(":", 1)[0]
                for line in passwd_file
                if ":" in line
            ]

        return "\n".join(users) + "\n"

    except OSError as e:
        return f"Error leyendo /etc/passwd: {e}\n"


def get_user_aliases():
    """
    Busca alias definidos en .bashrc y .bash_aliases.

    Los archivos se leen directamente desde Python en lugar
    de invocar un intérprete de shell.
    """

    alias_files = [
        Path.home() / ".bashrc",
        Path.home() / ".bash_aliases"
    ]

    aliases = []

    for file_path in alias_files:
        try:
            if file_path.exists():
                for line in file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines():

                    stripped = line.strip()

                    if stripped.startswith("alias "):
                        aliases.append(
                            f"{file_path.name}: {stripped}"
                        )

        except OSError as e:
            aliases.append(
                f"Error leyendo {file_path}: {e}"
            )

    if not aliases:
        return "No se encontraron alias configurados.\n"

    return "\n".join(aliases) + "\n"


# ============================================================
# Procesos
# ============================================================

def get_processes():
    return run_command(["ps", "aux"])


# ============================================================
# Red
# ============================================================

def get_open_ports():
    return run_command(["ss", "-tuln"])


def get_network_info():
    return run_command(["ip", "a"])


def get_network_routes():
    return run_command(["ip", "route"])


# ============================================================
# Sistema de archivos
# ============================================================

def get_mount_points():
    return run_command(["findmnt"])


def get_disk_usage():
    return run_command(["df", "-h"])


# ============================================================
# Permisos especiales
# ============================================================

def get_suid_files():
    return run_command(
        ["find", "/", "-perm", "-4000"],
        timeout=60
    )


# ============================================================
# Logs del sistema
# ============================================================

def get_recent_logs():
    """
    Recupera únicamente los últimos eventos para evitar
    generar informes excesivamente grandes.
    """

    return run_command(
        ["journalctl", "-n", "30", "--no-pager"],
        timeout=30
    )


def get_warning_logs():
    """
    Recupera los últimos eventos con prioridad warning
    o superior.
    """

    return run_command(
        [
            "journalctl",
            "-p",
            "warning",
            "-n",
            "20",
            "--no-pager"
        ],
        timeout=30
    )

# ============================================================
# Resumen de seguridad
# ============================================================

def generate_security_summary(
    system_info,
    distribution_info,
    open_ports,
    suid_files,
    warning_logs
):
    """
    Genera un resumen informativo a partir de los datos
    recopilados por LinuxRecon.

    El resumen no clasifica automáticamente los elementos
    encontrados como vulnerabilidades, sino que identifica
    aspectos que pueden requerir revisión posterior.
    """

    # Número aproximado de sockets detectados.
    port_lines = [
        line for line in open_ports.splitlines()
        if line.startswith(("tcp", "udp"))
    ]

    # Número de archivos SUID.
    suid_lines = [
        line for line in suid_files.splitlines()
        if line.startswith("/")
    ]

    # Número de eventos warning recuperados.
    warning_lines = [
        line for line in warning_logs.splitlines()
        if line.strip()
        and not line.startswith("Advertencia")
        and not line.startswith("Error")
    ]

    # Extracción sencilla de la distribución.
    distribution = "No identificada"

    for line in distribution_info.splitlines():
        if line.startswith("PRETTY_NAME="):
            distribution = line.split("=", 1)[1].strip('"')
            break

    architecture = "No identificada"

    if "aarch64" in system_info.lower():
        architecture = "aarch64 / ARM64"
    elif "x86_64" in system_info.lower():
        architecture = "x86_64"

    summary = f"""
=================================================
           RESUMEN DE SEGURIDAD
=================================================

Sistema:
  Distribución: {distribution}
  Arquitectura: {architecture}

Resultados de recopilación:
  Sockets detectados: {len(port_lines)}
  Archivos con permiso SUID: {len(suid_lines)}
  Eventos warning recopilados: {len(warning_lines)}

Aspectos de interés para revisión:

[+] Información general del sistema recopilada.
[+] Identidad y usuarios analizados.
[+] Interfaces y rutas de red recopiladas.
[+] Puertos y sockets en escucha identificados.
[+] Puntos de montaje y uso de disco recopilados.
[+] Archivos con permisos SUID identificados.
[+] Logs recientes del sistema recopilados.

[!] Los archivos SUID detectados deben ser revisados
    individualmente para determinar si su presencia es necesaria.

[!] Los puertos y sockets identificados deben contrastarse
    con los servicios que deberían estar expuestos.

[!] Los warnings del sistema pueden requerir una revisión
    adicional por parte del administrador.

IMPORTANTE:
La presencia de un archivo SUID, un puerto abierto o un warning
no implica por sí misma la existencia de una vulnerabilidad.

Estado de la recopilación: COMPLETADA
=================================================
"""

    return summary

# ============================================================
# Generación del reporte
# ============================================================

def generate_report():
    print("[+] Generando reporte...")

    # --------------------------------------------------------
    # Recopilación
    # --------------------------------------------------------

    system_info = get_system_info()
    distribution_info = get_distribution_info()

    current_user = get_current_user()
    user_id = get_user_id()
    all_users = get_all_users()
    user_aliases = get_user_aliases()

    processes = get_processes()

    open_ports = get_open_ports()
    network_info = get_network_info()
    network_routes = get_network_routes()

    mount_points = get_mount_points()
    disk_usage = get_disk_usage()

    suid_files = get_suid_files()

    recent_logs = get_recent_logs()
    warning_logs = get_warning_logs()

    # --------------------------------------------------------
    # Resumen
    # --------------------------------------------------------

    security_summary = generate_security_summary(
        system_info,
        distribution_info,
        open_ports,
        suid_files,
        warning_logs
    )

    # --------------------------------------------------------
    # Construcción del informe
    # --------------------------------------------------------

    report = f"""
=================================================
            LinuxRecon Security Report
=================================================
Fecha: {datetime.now()}

[INFORMACIÓN GENERAL DEL SISTEMA]
{system_info}

[DISTRIBUCIÓN Y VERSIÓN]
{distribution_info}

[USUARIO ACTUAL]
{current_user}

[ID DEL USUARIO]
{user_id}

[USUARIOS DEL SISTEMA]
{all_users}

[ALIAS DEL USUARIO]
{user_aliases}

[PROCESOS EN EJECUCIÓN]
{processes}

[PUERTOS ABIERTOS]
{open_ports}

[INFORMACIÓN DE RED]
{network_info}

[RUTAS DE RED]
{network_routes}

[PUNTOS DE MONTAJE]
{mount_points}

[USO DE SISTEMAS DE ARCHIVOS]
{disk_usage}

[ARCHIVOS CON PERMISOS SUID]
{suid_files}

[LOGS RECIENTES]
{recent_logs}

[WARNINGS DEL SISTEMA]
{warning_logs}

{security_summary}

=================================================
Fin del reporte
=================================================
"""

    try:
        REPORT_FILE.write_text(
            report,
            encoding="utf-8"
        )

        # El informe contiene información potencialmente
        # sensible y solo será accesible por su propietario.
        REPORT_FILE.chmod(0o600)

        print(
            "[+] Reporte generado correctamente: "
            f"{REPORT_FILE}"
        )

    except OSError as e:
        print(
            f"[-] Error al generar el reporte: {e}"
        )


# ============================================================
# Menú principal
# ============================================================

def main():
    print("===================================")
    print("      LinuxRecon - TFM Tool")
    print("===================================")
    print("1. Generar reporte completo")
    print("2. Salir")

    option = input(
        "Selecciona una opción: "
    ).strip()

    if option == "1":
        generate_report()

    elif option == "2":
        print("Saliendo...")

    else:
        print("Opción no válida.")


# ============================================================
# Ejecución
# ============================================================

if __name__ == "__main__":
    main()
