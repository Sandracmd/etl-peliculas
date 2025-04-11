from etl.extract import ExcelExtractor
from etl.transform import Transformer
from etl.load import save_to_csv

def main():
    path = "data/Films_2.xlsx"
    extractor = ExcelExtractor(path)
    data = extractor.read_all_sheets()

    transformer = Transformer(data)
    merged_df = transformer.join_films_inventory_rental()
    rental_stats = transformer.calculate_rental_stats(merged_df)

    print("\n Top 10 películas más alquiladas:")
    print(rental_stats.head(10))

    save_to_csv(rental_stats)

if __name__ == "__main__":
    main()
