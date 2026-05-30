from src import config
import pandas as pd
import matplotlib.pyplot as plt

def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el número total de partidos jugados por cada equipo
    """

    home = data["HomeTeam"].value_counts()
    away = data["AwayTeam"].value_counts()

    matches_team_total = (home + away).reset_index()

    matches_team_total.columns = ["Equipo","N_Partidos"]

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html --> .reset_index(drop=True)
    matches_team_total = (matches_team_total.sort_values(by="N_Partidos",ascending=False)).reset_index(drop=True)

    return matches_team_total



def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """
    Crea figura del número total de partidos jugados por cada equipo
    """

    plt.figure(figsize=(13,8))

    plt.bar(matches_team_total["Equipo"], matches_team_total["N_Partidos"])

    plt.xticks(rotation=82)

    plt.xlabel("Equipos")
    plt.ylabel("Número partidos")
    plt.title("Partidos totales por equipo")

    plt.savefig(f"src/img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
