# Guía de uso

## 1. Comprobar el entorno

```bash
python3 --version
```

LinuxRecon está pensado para ejecutarse en Linux.

## 2. Ejecutar LinuxRecon

Desde la raíz del repositorio:

```bash
python3 my.py
```

Selecciona la opción `1` para generar el reporte completo.

## 3. Consultar el informe

```bash
less report.txt
```

También pueden consultarse secciones concretas, por ejemplo:

```bash
grep -A3 "\[USUARIO ACTUAL\]" report.txt
grep -A12 "\[PUERTOS ABIERTOS\]" report.txt
grep -A20 "\[ARCHIVOS CON PERMISOS SUID\]" report.txt
```

## 4. Medir una ejecución

```bash
time python3 my.py
```

Para consultar el tamaño y el número de líneas del informe:

```bash
ls -lh report.txt
wc -l report.txt
```

## 5. Precaución con el informe

No publiques `report.txt` directamente. Revísalo y anonimízalo antes de compartirlo, ya que puede contener información del sistema analizado.
