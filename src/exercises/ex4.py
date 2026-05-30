from src import config
import pandas as pd
import matplotlib.pyplot as plt

def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """
    Devuelve dataframe con distribución de resultados: visctorias locales, victorias visitantes y empates.
    """

    full_time_res = data["FTR"].value_counts().reset_index()
    full_time_res.columns = ["Full_Time_Result", "Numero_Partidos"]

    return full_time_res


def plot_FTR(ftr: pd.DataFrame) -> None:
    """
    Representa los resultados finales
    """

    plt.figure(figsize=(9,6))

    plt.bar(ftr["Full_Time_Result"], ftr["Numero_Partidos"])

    plt.xlabel("Full Time Result")
    plt.ylabel("Número de partidos")
    plt.title("Distribución resultados finales")

    plt.savefig(f"src/img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
