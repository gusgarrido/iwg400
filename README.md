# Enigma

Aplicación web del grupo Enigma (11) para la asignatura IWG400 (Proyecto Inicial).

> [!WARNING]
> Este es un proyecto de concepto y prototipo. No se asegura funcionalidad real. Los autores no se hacen responsables de cualquier daño.

# Instalación

## Requisitos

Asegura tener instalado las siguientes dependencias:
- [Git](https://git-scm.com/install/windows)
- [Python 3.14+](https://www.python.org/downloads/)

## Clonar el repositorio e instalar dependencias

Ejecuta el siguiente comando en el terminal para descargar los archivos a la máquina local e instalar las dependencias:

```cmd
git clone https://github.com/gusgarrido/iwg400.git
cd iwg400
py -3 -m pip install -r requirements.txt
```

> [!NOTE]
> Si utilizas Linux, cambia `py -3` por `python3`.

# Ejecución

Asegura que tu directorio activo sea el nivel más alto de este proyecto. Para probar la página desde tu propia máquina, primero asegura tener la base de datos al día:

```cmd
python3 manage.py makemigrations
python3 manage.py migrate
```

Luego, puedes iniciar el servidor ejecutando el siguiente comando:

```
python3 manage.py runserver
```

Una vez listo, abre http://localhost:8000/ en el navegador.

# Licencia

Este proyecto se encuentra licenciado bajo la [Licencia de MIT](https://github.com/gusgarrido/iwg400/blob/main/LICENSE).