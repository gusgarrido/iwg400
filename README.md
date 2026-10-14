# Enigma

Aplicación web del grupo Enigma (11) para la asignatura IWG400 (Proyecto Inicial).

> [!WARNING]
> Este es un proyecto de concepto y prototipo. No se asegura funcionalidad real. Los autores no se hacen responsables de cualquier daño.

# Instalación

Antes de copiar el repositorio, asegura tener una llave SSH vinculada con tu cuenta de GitHub. Si no sabes qué es eso, revisa la siguiente documentación y sigue los pasos recomendados ahí:

- [Generación de una nueva clave SSH y adición al agente SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Agregar una clave SSH nueva a tu cuenta](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=windows&tool=webui)

## Requisitos

Asegura tener instalado las siguientes dependencias ya instaladas:
- [Git](https://git-scm.com/install/windows)
- [Python 3.14+](https://www.python.org/downloads/)

## Clonar el repositorio e instalar dependencias

Ejecuta el siguiente comando en el terminal para descargar los archivos a la máquina local:

```cmd
git clone git@github.com:gusgarrido/iwg400
py -3 -m pip install -r requirements.txt
```

> [!NOTE]
> Si utilizas Linux, cambia `py -3` por `python3`.

# Ejecución

Asegura que tu directorio activo sea el nivel más alto de este proyecto. Para probar la página desde su propia máquina, ejecuta el siguiente comando:

```cmd
python manage.py runserver
```

Luego, abre http://localhost:8000/ en el navegador.

# Licencia

Este proyecto se encuentra licenciado bajo la [Licencia de MIT](https://github.com/gusgarrido/iwg400/blob/main/LICENSE).