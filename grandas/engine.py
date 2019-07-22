from py2neo import Graph


def graph_engine(engine, **kwargs):
    if engine == "neo4j":
        return Graph(**kwargs)
    else:
        raise Exception("Sorry, we haven't implemented that engine yet.")


