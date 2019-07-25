"""Initial graph object"""
from pandas import DataFrame, Series

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
        # Make this from the Nodes class below

        return Series(nodes)

    def make_relationships(self):
        pass

    def head(self, n=5, r=15):
        # NOTE: Head should return the top 5 (by default) nodes, and all the
        # relationships associated with those 5 nodes (up to a limit of, say 10?)

        # NOTE: This should display two distinct dataframes, so should have some
        # edited settings in jupyter notebook:
        # https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side
        pass


class Nodes(DataFrame):
    """Extends a pandas DataFrame to initialize for Node objects in grandas"""

    def __init__(self, nodes: list):
        super(DataFrame, self).__init__()

        all_columns = list(set([n.keys() for n in nodes]))


class Relationships(DataFrame):
    """Extends a pandas DataFrame to initialize for Relationship objects in grandas"""

    def __init__(self, relationships: list):
        super(DataFrame, self).__init__()

    def expand(self):
        """
        Method takes the nodes that are multi-indexed in Relationships and expands
        out the properties in each of them, for a dataframe with the full set of
        all details on the entity-relationship pairs.
        """
        pass

    def invert(self, label="label"):
        """
        Examines the entities and relationships available based on entity type or
        another field
        """
        pass
