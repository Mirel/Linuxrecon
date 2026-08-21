# Seguridad

## Alcance de seguridad

LinuxRecon está diseñado para recopilar información local mediante operaciones principalmente de consulta. No modifica deliberadamente usuarios, procesos, servicios, interfaces de red ni configuraciones del sistema.

## Información sensible

El archivo `report.txt` puede contener información sensible del equipo analizado, por ejemplo:

- nombre del host y arquitectura;
- usuarios y grupos;
- procesos activos;
- puertos en escucha;
- interfaces y direcciones de red;
- rutas de archivos SUID.

Por este motivo, `report.txt` está incluido en `.gitignore`. No publiques informes reales sin revisarlos y anonimizar previamente la información que pueda identificar el sistema.

## Consideraciones de la versión actual

La función `run_command()` utiliza `subprocess.run(..., shell=True)`. Los comandos ejecutados están definidos dentro del código y la interfaz actual no permite al usuario introducir comandos arbitrarios. Aun así, una evolución futura debería valorar el uso de `shell=False` y listas de argumentos controladas para reducir la superficie de riesgo.

También se recomienda aplicar permisos restrictivos a los informes generados en futuras versiones.

## Uso autorizado

Utiliza la herramienta únicamente en sistemas propios o con autorización expresa.
