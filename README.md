# PEC4 CHIURAZZI LORENZO - Análisis histórico de LaLiga (1995-2025)

## Estructura del proyecto

```text
.
src/
    config.py
    data/
        LaLiga_Matches.csv
    exercises/
        ex1.py
        ...
    img/
    .png
    ...
tests/
    __init__.py
    test_ex6.py
doc/
    doc_ex1.html
    ...
screenshots/
    .png
    ...
requirements.txt
main.py
LICENSE
README.md
```


## Instalación

Crear un entorno virtual:
>python -m venv .venv

Activar el entorno:
>.venv\Scripts\activate

Instalar dependencias:
>pip install -r requirements.txt


## Ejecución del proyecto

Ejecutar todos los ejercicios:
>python main.py

Ejecutar hasta un ejercicio concreto:
>python main.py -ex 5


## Comprobación  linting

Instalar **pylint**:
>pip install pylint

Ejecutar el análisis:
>pylint main.py 

>pylint src/exercises


## Generación de documentación

La documentación se genera mediante **pydoc**.

Ejemplo:
>python -m pydoc -w src.exercises.ex1

Los archivos HTML generados se almacenan en la carpeta doc/


## Tests

Se ha implementado un test unitario para comprobar el correcto funcionamiento de la función `fun_total_goals()` definida en el ejercicio 6.

El test se encuentra en:
>tests/TEST_fun_total_goals.py

Para ejecutar el test:
>python -m unittest tests/TEST_fun_total_goals.py


## Requirements
Las librerías asociadas al proyecto se encuentran en el fichero `requirements.txt`


## Licencia
`MIT License`

## GitHub

Agrega todos los archivos al área de preparación
>git add .

Crea un commit:
>git commit -m "Versión <número_versión>"

Enviar a GitHub:
>git push


## Instalación mediante setup.py

El proyecto incluye un fichero `setup.py` que permite instalar automáticamente las librerías necesarias.

Para realizar la instalación desde la carpeta raíz del proyecto:
>pip install .

o
>python -m pip install .