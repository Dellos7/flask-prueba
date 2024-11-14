# Pruebas Flask

## Instalar Flask

### En el ordenador/MV
```bash
sudo apt install python3.8-venv
```

### Para crear el proyecto
Crear una carpeta para el proyecto

Después (dentro de la carpeta) creamos y activamos el entorno virtual:
```bash
python3 -m venv .venv
. .venv/bin/activate
```

Instalamos flask dentro del entorno virtual:
```bash
pip install Flask
```

## Lanzar app
```bash
flask --app hello.py run --debug
```

Si añadimos la opción `--host=0.0.0.0` se podrá hacer visible a toda la red
