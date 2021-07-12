# Scrapper de ofertas abiertas de Software de LinkedIn para CABA

## Contenidos
  * .spyproject/config : Archivos de configuración de proyecto en Spyder
  * Chrome/: Carpeta que contiene contenidos relativos a Google chrome.
    * Chromedata/: Carpeta que contiene cookies con el usuario logeado de Linkedin y preferencias de usuario seteadas.
      * cookies.pkl: Cookies en formato pickle.
    * ChromeSetup.exe: Instalador de Google Chrome Ver. 91.
    * chromedriver.exe: Chromedriver para usar con Selenium, compatible con Chrome Ver. 91.
  * file/: Carpeta en la cual se descarga la última tabla subida
    * sofware_emp.csv: datos de la tabla subida en formato csv
  * client_secrets.json: json de uso de app autorizada a la API de Google Drive
  * mycreds.txt: credenciales oauth de autenticación de usuario
  * script.py: programa
  
Descripcion de Script.py:
  El script inicializa una instancia de Selenium con chromedriver, se logea en la página de linkedin, busca empleos de Software con filtros de CABA y parsea el resultado adjuntándole la fecha de la corrida.
  Se descargan los datos del día anterior de Google Drive, se suman los datos nuevos, y se vuelven a subir pisando el archivo.
  
    
    
