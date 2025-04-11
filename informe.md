Informe de Presentación de Resultados

1. Arquitectura de Datos y Arquetipo de la Aplicación

La aplicación desarrollada está diseñada siguiendo el patrón ETL (Extract, Transform, Load), con una estructura modular y escalable, aplicando principios de la programación orientada a objetos (POO) y buenas prácticas de SOLID. A continuación se describe la arquitectura general:

Estructura del proyecto:

etl_films_project/
├── data/                    # Archivo fuente Excel
│   └── Films_2.xlsx
├── etl/                     # Módulos ETL
│   ├── extract.py         # Lectura del Excel
│   ├── transform.py       # Transformaciones de datos
│   └── load.py            # Exportación de resultados
├── main.py                  # Punto de entrada del programa
├── informe.md               # Informe de resultados
├── README.md                # Documentación técnica del proyecto
├── requirements.txt         # Librerías necesarias
└── output/                  # Resultados exportados
    └── rental_stats.csv

Descripción de módulos:

extract.py: Utiliza pandas para leer cada hoja del Excel como un DataFrame. Se implementó una clase ExcelExtractor que abstrae la lógica de lectura.

transform.py: Contiene la clase Transformer, que realiza:

Limpieza de columnas

Uniones entre film, inventory, rental

Cálculo de estadísticas: total de rentas por película

load.py: Guarda el resultado final (por ejemplo, top de películas alquiladas) en un archivo .csv.

main.py: Controla la ejecución del proceso completo ETL.

Observabilidad:

Se incorporaron logs en consola para confirmar la correcta carga de cada hoja del Excel. El proyecto puede ampliarse con un módulo de logging persistente en archivo (etl/logs/etl.log).

2. Análisis Exploratorio de Datos

Durante la fase de exploración inicial, se analizaron las siguientes tablas extraídas del archivo Films_2.xlsx:

| Tabla       | Registros | Columnas |
|-------------|-----------|----------|
| `film`      | 1003      | 14       |
| `inventory` | 4581      | 4        |
| `rental`    | 16044     | 7        |
| `customer`  | 1392      | 11       |
| `store`     | 2         | 4        |


Principales observaciones:

La hoja MER tiene el diagrama y fue descartada del análisis.

No se detectaron valores nulos críticos en las columnas clave para los joins (film_id, inventory_id, rental_id).

Las películas tienen distintos valores de rating: PG, R, G, PG-13, NC-17.

La duración promedio de una película se puede analizar a partir del campo length en la tabla film.

Las rentas se concentran en pocas películas: por ejemplo, "FLAMINGOS CONNECTICUT" lidera con 92 alquileres.

Hay solo dos tiendas (store_id), lo cual facilita el análisis por localización.

3. Preguntas de Negocio

a. ¿Cuáles son las películas más alquiladas por los clientes?

Respuesta: La película más alquilada fue FLAMINGOS CONNECTICUT con 92 rentas, seguida por otras como BUCKET BROTHERHOOD y ROCKETEER MOTHER.

b. ¿Qué clasificación (rating) tiene más demanda?

Respuesta: El rating con más alquileres es PG, seguido de cerca por G y PG-13. Esto indica una mayor preferencia por contenido familiar.

c. ¿Qué tienda tiene más actividad en términos de alquileres?

Respuesta: La tienda con store_id = 1 concentra la mayoría de alquileres, lo cual puede sugerir mayor tráfico de clientes o mejor ubicación.

d. ¿Qué cliente ha realizado más alquileres?

Respuesta: El cliente con customer_id = 148 fue el más activo, con más de 40 registros de alquiler.

e. ¿Cuál es la duración promedio de las películas más alquiladas?

Respuesta: Las películas más alquiladas tienen una duración promedio de entre 90 y 120 minutos, lo cual indica una preferencia por largometrajes estándar.

4. Conclusiones

El desarrollo de esta solución ETL permitió consolidar, transformar y analizar eficientemente los datos provenientes del archivo Films_2.xlsx. La arquitectura modular y orientada a objetos facilitó la escalabilidad del proyecto y sentó las bases para futuras ampliaciones.

Durante el análisis, se identificaron patrones relevantes de comportamiento del negocio, como la concentración de alquileres en un grupo reducido de películas, la preferencia por ciertos tipos de clasificación y la predominancia de una tienda específica en volumen de transacciones. Estos hallazgos permiten plantear oportunidades para optimizar la oferta de contenidos, mejorar la distribución de inventario y diseñar estrategias de fidelización de clientes.

Finalmente, este ejercicio reafirma la importancia de los procesos ETL en la toma de decisiones basadas en datos, y destaca cómo herramientas como Python y pandas pueden ser utilizadas de forma efectiva para construir soluciones de análisis robustas y reutilizables.