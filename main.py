import argparse
from src.exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7


if __name__ == "__main__":

    # https://ellibrodepython.com/python-argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-ex",
        type=int,
        default=7,
        help="Ejecuta ejercicios hasta el número indicado"
    )

    args = parser.parse_args()

    if args.ex >= 1:
        print("\n\nEX1-------------------------------------------------------------------------\n")
        #Funciones ex1

        data = ex1.load_and_eda(r"src/data/LaLiga_Matches.csv")

        ex1.plot_home_away_goals(data)

    if args.ex >= 2:
        print("\n\nEX2-------------------------------------------------------------------------\n")
        #Funciones ex2

        tot_matches = ex2.total_matches(data)
        print(f"\n10 primeros valores: \n{tot_matches.head(10)}")

        siempre_primera = tot_matches.loc[tot_matches["N_Partidos"] == tot_matches["N_Partidos"].max(), "Equipo"]
        print(f"\nEquipos que siempre han estado en primera: \n{siempre_primera}")

        ex2.plot_matches_team_total(tot_matches)

    if args.ex >= 3:
        print("\n\nEX3-------------------------------------------------------------------------\n")
        #Funciones ex3

        distr_goals_home, distr_goals_away = ex3.goals_distribution(data)
        print(f"\nDistribución goles locales: \n {distr_goals_home}")
        print(f"\nDistribución goles visitantes: \n {distr_goals_away}")

        ex3.plot_goals_distribution(distr_goals_home, distr_goals_away)

    if args.ex >= 4:
        print("\n\nEX4-------------------------------------------------------------------------\n")
        #Funciones ex4

        ftr = ex4.FTR(data)
        print(f"\nDistribución resultados: \n{ftr}")

        num_victorias_local = ftr.loc[ftr["Full_Time_Result"]=="H", "Numero_Partidos"]
        num_partidos_tot = ftr["Numero_Partidos"].sum()
        print(f"\nPorcentaje victorias equipo local: \n{(100 * num_victorias_local[0]) / num_partidos_tot:.2f}")

        ex4.plot_FTR(ftr)

    if args.ex >= 5:
        print("\n\nEX5-------------------------------------------------------------------------\n")
        #Funciones ex5
        df_puntos = ex5.add_points(data)
        print(f"\n10 primeros valores, dataframe con puntos: \n{df_puntos.head(10)}")

        puntos_equipos = ex5.fun_total_points(df_puntos)
        print(f"\n10 primeros valores, dataframe con puntos por equipo: \n{puntos_equipos.head(10)}")

        equipo_ganador =  ex5.alltime_winner(puntos_equipos)
        print(f"\nEquipo que ha acumulado más puntos: \n{equipo_ganador}")

    if args.ex >= 6:
        print("\n\nEX6-------------------------------------------------------------------------\n")
        #Funciones ex6
        goles = ex6.fun_total_goals(data)
        print(f"\n Goles Home Team, Goles Away Team, Goles Totales: \n{goles}")

        goles_equipos = ex6.fun_total_goals_by_team(df_puntos)
        print(f"\n 10 primeros valores de total_goals_by_team: \n{goles_equipos[2].head()}")

        summary_1996_2025 = ex6.fun_summary_1996_2025(puntos_equipos,goles_equipos[0],goles_equipos[1],goles_equipos[2])
        print(f"\n Primeros valores de summary_1996_2025: \n{summary_1996_2025.head(10)}")

        ex6.podium(summary_1996_2025)

    if args.ex >= 7:
        #Funciones ex7
        ex7.graf(data, summary_1996_2025["Equipo"].head(5).tolist())




