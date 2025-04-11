import pandas as pd

class Transformer:
    def __init__(self, data_loader: dict):
        self.data_loader = {
            k: v for k, v in data_loader.items()
            if v is not None and not v.empty and k.strip().lower() != "mer"
        }

        for df in self.data_loader.values():
            df.columns = df.columns.astype(str).str.strip()

    def join_films_inventory_rental(self):
        film_df = self.data_loader.get("film")
        inventory_df = self.data_loader.get("inventory")
        rental_df = self.data_loader.get("rental")

        if film_df is None or inventory_df is None or rental_df is None:
            print("Error, faltan tablas necesarias para hacer la union")
            return pd.DataFrame()

        merged_1 = pd.merge(film_df, inventory_df, on="film_id", how="inner")

        merged_2 = pd.merge(merged_1, rental_df, on="inventory_id", how="inner")

        return merged_2

    def calculate_rental_stats(self, merged_df):
        if merged_df.empty:
            print("No hay datos para calcular estadisticas")
            return pd.DataFrame()

        rental_counts = (
            merged_df.groupby("title")
            .agg(total_rentals=pd.NamedAgg(column="rental_id", aggfunc="count"))
            .reset_index()
            .sort_values(by="total_rentals", ascending=False)
        )

        return rental_counts
