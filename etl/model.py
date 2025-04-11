from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pandas as pd

def entrenar_modelo_rf(df, columnas_features, columna_objetivo):
    X = df[columnas_features]
    y = df[columna_objetivo]

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)

    df["pred_rf"] = modelo.predict(X)
    r2 = r2_score(y, df["pred_rf"])

    return modelo, r2, df