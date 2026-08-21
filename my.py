import subprocess
from datetime import datetime

# ==============================
# Función para ejecutar comandos
# ==============================
def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.stdout.strip():
            return result.stdout

        if result.stderr.strip():
            return f"Advertencia: {result.stderr}"

        return "Sin resultados.\n"

    except Exception as e:
        return f"Error ejecutando comando: {e}\n"

# ==============================
# Módulos de recolección
# ==============================

def get_system_info():
    return run_command("uname -a")

def get_current_user():
    return run_command("whoami")

def get_all_users():
    return run_command("cut -d: -f1 /etc/passwd")

def get_user_id():
    return run_command("id")

def get_processes():
    return run_command("ps aux")

def get_open_ports():
    return run_command("ss -tuln")

def get_network_info():
    return run_command("ip a")

def get_suid_files():
    return run_command("find / -perm -4000 2>/dev/null")

# ==============================
# Generación de reporte
# ==============================

def generate_report():
    print("[+] Generando reporte...")

    report = f"""
=================================================
            LinuxRecon Security Report
=================================================
Fecha: {datetime.now()}

[INFORMACIÓN DEL SISTEMA]
{get_system_info()}

[USUARIO ACTUAL]
{get_current_user()}

[ID DEL USUARIO]
{get_user_id()}

[USUARIOS DEL SISTEMA]
{get_all_users()}

[PROCESOS EN EJECUCIÓN]
{get_processes()}

[PUERTOS ABIERTOS]
{get_open_ports()}

[INFORMACIÓN DE RED]
{get_network_info()}

[ARCHIVOS CON PERMISOS SUID]
{get_suid_files()}

=================================================
Fin del reporte
=================================================
"""

    with open("report.txt", "w") as f:
        f.write(report)

    print("[+] Reporte generado correctamente: report.txt")

# ==============================
# Menú principal
# ==============================

def main():
    print("===================================")
    print("      LinuxRecon - TFM Tool")
    print("===================================")
    print("1. Generar reporte completo")
    print("2. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        generate_report()
    else:
        print("Saliendo...")

# ==============================
# Ejecución
# ==============================

if __name__ == "__main__":
    main()
