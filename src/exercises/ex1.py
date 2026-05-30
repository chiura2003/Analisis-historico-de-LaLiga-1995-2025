import pandas as pd
import matplotlib.pyplot as plt
from src import config

def load_and_eda(file: str) -> pd.DataFrame:
    """
    Carga el dataset, elimina columnas "HTHG", "HTAG", "HTR" y muestra resultados.
    """

    data = pd.read_csv(file)

    # eliminamos las columnas "HTHG", "HTAG", "HTR"

    data = data.drop(columns=["HTHG", "HTAG", "HTR"])

    # se muestran primeros, ùltimos valores y información
    print("\nPrimeros valores: ")
    print(data.head())

    print("\nÚltimos valores: ")
    print(data.tail())

    print("\nInformación del dataset: ")
    print(data.info())

    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """
    Figura con dos gráficos sobre la distribución de goles en casa y fuera
    """

    plt.figure(figsize=(8, 5))

    #https://www.codecademy.com/resources/docs/matplotlib/pyplot/boxplot
    plt.boxplot([data["FTHG"], data["FTAG"]], labels=["Home", "Away"])

    plt.title("Distribución de goles")
    plt.ylabel("Número de goles")
    plt.savefig(f"src/img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
