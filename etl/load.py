import os

def save_to_csv(df, output_path="output/rental_stats.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        df.to_csv(output_path, index=False)
        print(f"Ok, archivo guardado correctamente en {output_path}")
    except Exception as e:
        print(f"Error, no se pudo guardar el archivo {e}")
