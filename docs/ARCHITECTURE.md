# Arquitectura de LinuxRecon

LinuxRecon utiliza una arquitectura funcional sencilla y adecuada al alcance del prototipo.

## Componentes principales

### `main()`

Punto de entrada de la aplicación. Presenta el menú y recibe la opción seleccionada por el usuario.

### `generate_report()`

Coordina las funciones de recopilación y construye el informe final `report.txt`.

### `run_command()`

Centraliza la ejecución de comandos del sistema mediante `subprocess.run()` y recoge por separado la salida estándar y la salida de error.

### Funciones de recopilación

| Función | Operación |
| --- | --- |
| `get_system_info()` | Información general del sistema |
| `get_current_user()` | Usuario actual |
| `get_user_id()` | UID, GID y grupos |
| `get_all_users()` | Usuarios registrados |
| `get_processes()` | Procesos activos |
| `get_open_ports()` | Puertos y sockets en escucha |
| `get_network_info()` | Interfaces y direcciones de red |
| `get_suid_files()` | Archivos con permisos SUID |

## Flujo

```text
Usuario
  |
  v
main()
  |
  v
generate_report()
  |
  +--> get_system_info()
  +--> get_current_user()
  +--> get_user_id()
  +--> get_all_users()
  +--> get_processes()
  +--> get_open_ports()
  +--> get_network_info()
  +--> get_suid_files()
          |
          v
     run_command()
          |
          v
      Sistema Linux
          |
          v
      report.txt
```

## Evolución

Una versión posterior puede separar físicamente el proyecto en `core/`, `modules/`, `reports/` y `plugins/`, manteniendo el núcleo como coordinador y permitiendo añadir nuevos módulos de análisis.
