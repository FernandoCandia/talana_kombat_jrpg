#  Talana Kombat JRPG
 Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

## Pre-requisitos
-   Docker 25.0.3^

##  Instalación

### Alternativa 1 - DockerHub

Descarga la imagen Docker del proyecto con el siguiente comando en consola:

```sh
docker pull fdojavier2/talana_kombat_jrpg:1.0.0
```

Ejecuta el contenedor con:

```sh
docker run -it --rm -p 8000:80 fdojavier2/talana_kombat_jrpg:1.0.0
```

Finalmente, accede a http://localhost:8000 y comienza a utilizar la aplicación.

### Alternativa 2 - GitHub + Docker

Clona el siguiente repositorio:

```sh
git clone https://github.com/FernandoCandia/talana_kombat_jrpg.git
```

En consola, asegúrate de estar en la carpeta root del repositorio:

```sh
cd talana_kombat_jrpg 
```

Luego, crea la imagen de Docker con:

```sh
docker build -t talana_kombat_jrpg . 
```

Ejecuta el contenedor con:

```sh
docker run -it --rm -p 8000:80 fdojavier2/talana_kombat_jrpg:1.0.0
```

Finalmente, accede a http://localhost:8000 y comienza a utilizar la aplicación.

## Interacción con aplicación web
Cargar archivo JSON con los ejemplos que aparecen en el mismo directorio del proyecto django o cualquier otro archivo JSON con el formato de entrada correspondiente.

En base a los datos de entrada en formato JSON se relatará la pelea y el resultado final.

## Tests

Mientras está corriendo el servidor en Docker, puedes ejecutar los tests del proyecto django abriendo una consola de powershell que también apunte al root del proyecto (Importante: no debes terminar la ejecución del servidor en la consola anterior):

```sh
docker ps -q | Select-Object -Last 1 | ForEach-Object { docker exec -it $_ bash }
cd kombat/
pytest
```
