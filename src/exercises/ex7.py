from src import config
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def graf(data: pd.DataFrame, selected_teams: list) -> None:
    """
    Genera un grafo con networkx

    Fuentes:
        https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_edge_labels.html
        https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.get_edge_attributes.html
        https://cienciadedatos.net/documentos/pygml03-analisis-redes-python-networkx
        https://networkx-org.translate.goog/documentation/stable/tutorial.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sge
        https://stackoverflow.com/questions/16476924/how-can-i-iterate-over-rows-in-a-pandas-dataframe
        https://www.geeksforgeeks.org/python/pandas-groupby-count-the-occurrences-of-each-combination/
        https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe
        https://www.ellaberintodefalken.com/2020/02/grafos-con-networkx.html
        #https://stackoverflow.com/questions/9764603/updating-weight-information-depending-on-repeat-of-edges-with-networkx

    """

    #https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe
    filtered_data = data[(data["HomeTeam"].isin(selected_teams)) & (data["AwayTeam"].isin(selected_teams))]

    #https://www.geeksforgeeks.org/python/pandas-groupby-count-the-occurrences-of-each-combination/ para usar .size()
    connections = (filtered_data.groupby(["HomeTeam", "AwayTeam"]).size().reset_index(name="Partidos"))

    #https://www.ellaberintodefalken.com/2020/02/grafos-con-networkx.html
    G = nx.Graph()

    G.add_nodes_from(selected_teams)

    for _, fila in connections.iterrows():

        local = fila["HomeTeam"]
        visitante = fila["AwayTeam"]
        partidos = fila["Partidos"]

        #https://stackoverflow.com/questions/9764603/updating-weight-information-depending-on-repeat-of-edges-with-networkx
        if G.has_edge(local, visitante):
            G[local][visitante]["jugados"] += partidos
        else:
            G.add_edge(local, visitante, jugados=partidos)
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G, seed=90)

    nx.draw(G, pos, with_labels=True, node_size=1300, font_size=20)

    #https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.get_edge_attributes.html
    etiqueta = nx.get_edge_attributes(G, "jugados")

    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiqueta)

    plt.savefig(f"src/img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png")