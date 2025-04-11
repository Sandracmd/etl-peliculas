import pandas as pd

class ExcelExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_sheet(self, sheet_name):
        try:
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            print(f"OK, hoja cargada '{sheet_name}' con {len(df)} filas.")
            return df
        except Exception as e:
            print(f"Error, hoja no cargada '{sheet_name}': {e}")
            return None

    def read_all_sheets(self):
        try:
            xl = pd.ExcelFile(self.file_path)
            dataframes = {sheet: self.read_sheet(sheet) for sheet in xl.sheet_names}
            return dataframes
        except Exception as e:
            print(f"Errror, no se pudo abrir el archivo {e}")
            return {}
