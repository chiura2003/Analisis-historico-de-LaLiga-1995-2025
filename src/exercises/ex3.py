from src import config
import pandas as pd
import matplotlib.pyplot as plt


def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Genera dos Dataframes con distribución de goles de  los equipos locales y visitantes
    """

    distr_goals_home = data["FTHG"].value_counts().sort_index().reset_index()
    distr_goals_home.columns = ["Goles", "Numero_Partidos"]
    distr_goals_away = data["FTAG"].value_counts().sort_index().reset_index()
    distr_goals_away.columns = ["Goles", "Numero_Partidos"]

    return distr_goals_home, distr_goals_away

def plot_goals_distribution(distr_goals_home: pd.DataFrame, distr_goals_away: pd.DataFrame) -> None:
    """
    Representa la distribución de goles de equipos locales y visitantes.
    """

    #https://interactivechaos.com/es/manual/tutorial-de-matplotlib/la-funcion-subplots
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    ax[0].bar(distr_goals_home["Goles"], distr_goals_home["Numero_Partidos"])
    ax[0].set_title("Goles Home Team")
    ax[0].set_xlabel("Número de goles")
    ax[0].set_ylabel("Número de partidos")

    ax[1].bar(distr_goals_away["Goles"], distr_goals_away["Numero_Partidos"])
    ax[1].set_title("Goles Away Team")
    ax[1].set_xlabel("Número de goles")
    ax[1].set_ylabel("Número de partidos")

    plt.savefig(f"src/img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
