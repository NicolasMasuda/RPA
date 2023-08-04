# Descarga de Cartola Banco Santander Chile - RPA con Selenium

Este script de Python utiliza el framework Selenium para automatizar el proceso de descarga de la cartola de una cuenta en el Banco Santander de Chile. La automatización se enfoca en RPA (Automatización de Procesos Robóticos) y permite realizar el inicio de sesión en el sitio web del banco y descargar la cartola de la cuenta asociada.

## ¿Cómo funciona?

El script simula las acciones que un usuario realizaría manualmente para acceder a la cartola de su cuenta en el sitio web del Banco Santander de Chile. A continuación, se describen los pasos principales del proceso:

1. **Inicio de Sesión**: El script abre una ventana del navegador Chrome y navega a la página de inicio de sesión del Banco Santander. Luego, ingresa las credenciales de inicio de sesión (RUT y contraseña) proporcionadas en las variables `id` y `contrasena`, respectivamente. Después de enviar los datos, espera un tiempo para permitir que se complete el inicio de sesión.

2. **Acceso a Cartolas**: Una vez que el inicio de sesión es exitoso, el script navega a la sección de "Cuentas" en la página web y selecciona la opción de "Cartolas" para acceder a las cartolas de la cuenta.

3. **Descarga de Cartola**: Una vez en la sección de "Cartolas", el script realiza clic en el botón de descarga de la cartola. Dependiendo de la configuración del sitio web, es posible que se abra una nueva ventana emergente para descargar el archivo de la cartola.

4. **Finalización**: Una vez que se ha completado la descarga de la cartola, el script espera un tiempo para permitir que se descargue completamente el archivo. Luego, cierra el navegador Chrome y finaliza la ejecución del script.

## Requisitos

- Python 3.x instalado en tu sistema.
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible con tu versión de Google Chrome. Asegúrate de colocar el archivo `chromedriver` en una ubicación accesible y actualiza la variable `pathDriverChrome` con la ruta completa a este archivo.
- El framework Selenium para Python, que se puede instalar con `pip`:

```bash
pip install selenium
```

## Uso

1. Descarga y coloca el archivo `chromedriver` en una ubicación accesible en tu sistema.
2. Modifica las variables `pathDriverChrome`, `id` y `contrasena` en el código con la ubicación del archivo `chromedriver` y tus credenciales de inicio de sesión del Banco Santander de Chile, respectivamente.
3. Ejecuta el script con Python:

```bash
python nombre_del_script.py
```

## Contribuciones

¡Contribuciones y mejoras son bienvenidas! Si deseas agregar más funcionalidades o realizar correcciones, por favor abre un `pull request` con tus cambios.

