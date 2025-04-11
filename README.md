PROYECTO ETL - ANÁLISIS DE PELÍCULAS Y RENTAS

Este proyecto implementa un proceso ETL utilizando Python para extraer, transformar y cargar datos del archivo Excel Films_2.xlsx. Se realiza un análisis de negocio para identificar las películas más alquiladas, preferencias por clasificación, actividad por tienda y comportamiento de los clientes.


TECNOLOGÍAS USADAS

Python 3.13+

pandas

openpyxl

Jupyter/VS Code (opcional)


ESTRUCTURA DEL PROYECTO

etl_films_project/
├── data/                    # Archivo fuente
│   └── Films_2.xlsx
├── etl/                     # Módulos del proceso ETL
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py                  # Script principal
├── informe.md               # Informe de resultados
├── README.md                # Este archivo
├── requirements.txt         # Dependencias
└── output/                # Resultados exportados
    └── rental_stats.csv

INSTALACIÓN

1. Clona el repositorio:

git clone <URL-del-repositorio>
cd etl_films_project

2. Crea un entorno virtual (opcional pero recomendado):

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

3. Instala las dependencias:

pip install -r requirements.txt


EJECUCIÓN DEL PROYECTO

1. Asegúrate de que el archivo Films_2.xlsx esté dentro de la carpeta data/.

2. Ejecuta el script principal:

python main.py

3. El resultado se guardará en output/rental_stats.csv y se mostrará por consola el top de películas más alquiladas.

MÓDULOS

- extract.py: lee las hojas del Excel y las convierte en DataFrames.

- transform.py: realiza joins, limpieza y genera estadísticas.

- load.py: guarda los datos transformados en CSV.

INFORME

Consulta el archivo informe.md para detalles técnicos, análisis y conclusiones del proyecto.