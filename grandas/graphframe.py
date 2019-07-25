"""Initial graph object"""
import pandas as pd

from .graph_objects import Node, Relationship


class GraphFrame:
    """docstring for GraphFrame."""

    a = "Hello test goodbye"

    def __init__(self, *args, **kwargs):
        if "nodes" in kwargs:
            self.nodes = self.make_nodes(nodes=kwargs["nodes"])  # Pandas DataFrame
        self.rels = self.make_relationships()

        if "graph" in kwargs:
            self.graph = graph

    def _make_graph(self, objs):
        pass

    def make_nodes(self, nodes):

        return pd.Series(nodes)

    def make_relationships(self):
        pass

    def head(self, n=5):
        # NOTE: Head should return the top 5 (by default) nodes, and all the
        # relationships associated with those 5 nodes (up to a limit of, say 10?)

        # NOTE: This should display two distinct dataframes, so should have some
        # edited settings in jupyter notebook:
        # https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side
        pass
