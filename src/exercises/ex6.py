from src import config
import pandas as pd
import matplotlib.pyplot as plt


def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """
    Genera tupla de tres elementos (goles locales, goles visitantes, goles totales)
    """

    home_goals = int(data["FTHG"].sum())

    away_goals = int(data["FTAG"].sum())

    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals




def fun_total_goals_by_team(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Calcula goles por equipo y devuelve tres DataFrame.
    """

    home_goals_by_team = data.groupby("HomeTeam")["FTHG"].sum()
    away_goals_by_team = data.groupby("AwayTeam")["FTAG"].sum()

    # suma goles para crear nueva series que convertiré en dataframe con reset_index()
    total_goals_by_team = (home_goals_by_team + away_goals_by_team).reset_index()
    total_goals_by_team.columns = ["Equipo", "Goles Totales"]
    total_goals_by_team = total_goals_by_team.sort_values(by="Goles Totales",ascending=False).reset_index(drop=True)

    # mejoro los dataframe home_goals_by_team y away_goals_by_team
    home_goals_by_team = home_goals_by_team.reset_index()
    away_goals_by_team = away_goals_by_team.reset_index()

    home_goals_by_team.columns = ["Equipo", "Goles como Local"]
    away_goals_by_team.columns = ["Equipo", "Goles como Visitante"]

    home_goals_by_team = home_goals_by_team.sort_values(by="Goles como Local",ascending=False).reset_index(drop=True)
    away_goals_by_team = away_goals_by_team.sort_values(by="Goles como Visitante",ascending=False).reset_index(drop=True)

    return home_goals_by_team, away_goals_by_team, total_goals_by_team



def fun_summary_1996_2025(
            total_points_by_team: pd.DataFrame,
            home_goals_by_team: pd.DataFrame,
            away_goals_by_team: pd.DataFrame,
            total_goals_by_team: pd.DataFrame
    ) -> pd.DataFrame:

    """
    Crea el dataframe a partir de la concatenación de los 4 dataframes que pasamos como argumentos
    """
    #https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/pandas-dataframe-merge-en-python/
    summary_1996_2025 = pd.merge(total_points_by_team,home_goals_by_team, on="Equipo")

    summary_1996_2025 = pd.merge(summary_1996_2025, away_goals_by_team, on="Equipo")

    summary_1996_2025 = pd.merge(summary_1996_2025, total_goals_by_team, on="Equipo")

    summary_1996_2025 = summary_1996_2025.sort_values(by="Puntos",ascending=False).reset_index(drop=True)

    return summary_1996_2025




def podium(summary_1996_2025: pd.DataFrame) -> None:
    """
    Genera una gráfica del podio
    """

    top = summary_1996_2025.head(3)

    #https://www.geeksforgeeks.org/pandas/get-a-specific-row-in-a-given-pandas-dataframe/
    teams = [top.iloc[1]["Equipo"], top.iloc[0]["Equipo"], top.iloc[2]["Equipo"]]

    heights = [2, 3, 1]
    colors = ["orange", "red", "yellow"]
    plt.figure(figsize=(7,7))

    bars = plt.bar(teams,heights,color=colors)

    #https://matplotlib.org/2.0.2/examples/api/barchart_demo.html para poner el nombre encima de la barra
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()+0.05, teams[i], ha="center")

    #eliminamos las etiquetas del eje x y del eje y
    plt.xticks([])
    plt.yticks([])

    plt.savefig(f"src/img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png")





