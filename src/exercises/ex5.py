import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Añade los puntos conseguidos como local y visitante.
    """

    # creo nueva columna y por cada línea añado el valor que le corresponde, utlizando .map()
    # https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map
    data["points_home"] = data["FTR"].map({"H": 3, "D": 1, "A": 0})

    data["points_away"] = data["FTR"].map({"H": 0, "D": 1, "A": 3})

    return data


def fun_total_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los puntos totales acumulados por cada equipo
    """

    #suma puntos según el equipo
    puntos_l = data.groupby("HomeTeam")["points_home"].sum()
    puntos_v = data.groupby("AwayTeam")["points_away"].sum()

    #suma puntos de los equipos entre los puntos conseguidos como local y como visitante, .reset_index() para convertirlo en dataframe
    df_total_points = (puntos_l + puntos_v).reset_index()

    df_total_points.columns = ["Equipo", "Puntos"]

    return df_total_points


def alltime_winner(df_total_points: pd.DataFrame) -> pd.DataFrame:
    """
    Devuelve el ganador histórico
    """

    equipo = df_total_points.loc[df_total_points["Puntos"] == df_total_points["Puntos"].max()].reset_index(drop=True)
    return equipo