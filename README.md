# aniPyFLV
DEPENDENCIAS:

  Dependencias externas a python:
  
    mpv: reproductor multimedia usado, facil de instalar en Windows, Linux y MacOS, con los episodios con mas info puede mostrar inicio/fin de opening y ending
    
    megatools: sirve para descargar episodios de MEGA
    
  Dependencias de python (en el momento de hacer este readme): 
  
    animeflv==0.3.1
    
    beautifulsoup4==4.13.4
    
    certifi==2025.4.26
    
    charset-normalizer==3.4.2
    
    cloudscraper==1.2.71
    
    idna==3.10
    
    lxml==5.4.0
    
    pyparsing==3.2.3
    
    requests==2.32.3
    
    requests-toolbelt==1.0.0
    
    soupsieve==2.7
    
    typing_extensions==4.13.2
    
    urllib3==2.4.0
    
    ***Es posible que en algunos casos se requiera de un entorno virtual para instalar las dependencias.
  

FUNCIONAMIENTO:

  Se trata de un programa por terminal hecho en python (se ejecuta como un programa normal de python), que nos pedirá el nombre del anime que queremos ver (puede ser español/japones, ojo con los nombres, y sensible a upper/lower case.
  
  Despues, aunque el anime exista, es posible que nos de error y se finalice el programa, ya que a veces estas apis o incluso MEGA tienen mecanismos para evitar cosas como peticiones directas al server (como hace esta app), basta con revisar si hemos escrito el nombre bien e insistir hasta que la ejecucion del programa continue normalmente.
  
  Luego de buscar el anime nos aparecera una serie de temporadas/episodios con un indice, seleccionamos el indice que queremos y se inicia la descarga del episodio.
  
  Si el programa falla en la etapa de busqueda/descarga puede ser debido a que algunos de estos videos de MEGA fueron tirados, en cuyo caso no los podremos ver (funciona relativamente bien con estrenos).
  
  Por ultimo, una vez se descargue el video en un directorio temporal (se limpia al bootear la maquina), se reproduce en mpv, hasta que acabe o que decidamos cerrar la ventana, matar la ejecucion del programa o similares.
