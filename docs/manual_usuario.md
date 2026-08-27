# Manual de usuario de LinuxRecon

## 1. Requisitos

LinuxRecon requiere un sistema Linux, Python 3 y las utilidades estándar empleadas por el programa.

## 2. Ejecución

Desde la raíz del repositorio:

```bash
python3 src/my.py
```

Seleccione `1` para generar el informe completo o `2` para salir.

## 3. Informe

La herramienta crea `report.txt` en el directorio desde el que se ejecuta. El archivo se protege con permisos `0600` porque puede contener información sensible del sistema.

Para consultarlo:

```bash
less report.txt
```

Para comprobar sus permisos:

```bash
ls -l report.txt
```

## 4. Interpretación

LinuxRecon recopila y organiza información. La aparición de un archivo SUID, un socket en escucha o un warning no demuestra por sí sola una vulnerabilidad; los resultados requieren revisión contextual.
