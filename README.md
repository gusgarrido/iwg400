# Enigma

Aplicación web del grupo Enigma (11) para la asignatura IWG400 (Proyecto Inicial).

Este es un proyecto de concepto y prototipo. No se asegura funcionalidad real.

# Instalación

Antes de copiar el repositorio, asegura tener una llave SSH vinculada con tu cuenta de GitHub. Si no sabe qué es eso, revisar la siguiente documentación y seguir los pasos recomendados ahí:

- [Generación de una nueva clave SSH y adición al agente SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Agregar una clave SSH nueva a tu cuenta](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=windows&tool=webui)

## Requisitos

Asegura tener instalado las siguientes dependencias:
- [Git](https://git-scm.com/install/windows)
- [Python 3.14+](https://www.python.org/downloads/)

## Clonar el repositorio e instalar dependencias

Ejecute el siguiente comando en su terminal para descargar los archivos a su máquina local:

```cmd
git clone git@github.com:gusgarrido/iwg400
py -3 -m pip install -r requirements.txt
```

Si está utilizando Linux, cambiar `py -3` por `python3`.

# Licencia

Este proyecto se encuentra licenciado bajo la [Licencia de MIT](https://github.com/gusgarrido/iwg400/blob/main/LICENSE).