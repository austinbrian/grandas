"""Initial graph object"""
from pandas import DataFrame, Series
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

from .graph_objects import Node, Relationship


class GraphFrame:
    """docstring for GraphFrame."""

    a = "Hello test goodbye"

    @property
    def _constructor(self):
        return GraphFrame

    @property
    def _constructor_sliced(self):
        return GraphFrame

    def __init__(self, nodes, relationships, *args, **kwargs):

        self.nodes = nodes
        self.relationships = relationships

        if "graph" in kwargs:
            self.graph = graph

        self.nframe = self.make_nodes(nodes=nodes)  # Pandas DataFrame
        self.rframe = self.make_relationships(relationships=relationships)

    def __repr__(self):
        display(
            self.nframe.style.set_caption("Nodes"),
            self.rframe.style.set_caption("Relationships"),
        )
        return (
            f"GraphFrame\nNodes: {len(self.nframe)}\nRelationships: {len(self.rframe)}"
        )

    def __getitem__(self, item):
        df = self.rframe.expand()
        # first try just applying them in order
        try:
            return df[item]

        # else try to build up the multiindex
        except KeyError:
            mindex = []
            for x in df.columns:
                if item in x:
                    mindex.append(x)
            return df[mindex]

    def __len__(self) -> int:
        """Length returns the number of nodes in the GraphFrame

        Returns
        -------
        int
            Number of nodes

        """
        return len(self.nframe)

    def info(self):
        self.nframe.info()
        self.rframe.info()

    @property
    def nf(self):
        return self.make_nodes(nodes=self.nodes)

    @property
    def rf(self):
        return self.make_relationships(relationships=self.relationships)

    def _make_graph(self, objs):
        pass

    def __repr_html__(self):
        # NOTE: This should display two distinct dataframes, so should have some
        # edited settings in jupyter notebook:
        # https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side
        pass

    def make_nodes(self, nodes):
        # Make this from the Nodes class below

        return NodeFrame(nodes=nodes)

    def make_relationships(self, relationships):
        # want to set the index here so it passes correctly
        return RelationshipFrame(relationships=relationships)

    def head(self, n=5, r=10):
        # NOTE: Head should return the top 5 (by default) nodes, and all the
        # relationships associated with those 5 nodes (up to a limit of, say 10?)

        nodes_to_return = self.nodes[:n]
        relationships_to_return = self.relationships[:r]

        # display(nodes_to_return, relationships_to_return)
        return GraphFrame(nodes=nodes_to_return, relationships=relationships_to_return)

    def resolve(self):
        # start by comparing hashes across the nodeframe
        pass

    def expand(self):
        return self.rframe.expand()


class NodeFrame(DataFrame):
    """Extends a pandas DataFrame to initialize for Node objects in grandas"""

    _metadata = ["nodes"]

    def __init__(self, nodes: list, *args, **kwargs):
        data = []
        for n in nodes:
            n_dict = dict(n)
            n_dict["hash_val"] = hash(n)
            data.append(n_dict)
        super().__init__(data=data, *args, **kwargs)

        self.nodes = nodes

    def resolve(self):
        # Broken by
        # TypeError: 'BlockManager' object is not iterable
        df_copy = self.copy()
        hash_df = pd.DataFrame(df_copy.nodes(), columns=["nodes"])
        hash_df["hash"] = hash_df.nodes.apply(hash)
        deduped_table = hash_df.drop_duplicates("hash")
        return deduped_table

    def to_df(self):
        return pd.DataFrame([dict(x) for x in self.nodes])


class RelationshipFrame(DataFrame):
    """Extends a pandas DataFrame to initialize for Relationship objects in grandas"""

    _metadata = ["relationships"]

    def __init__(self, relationships: list, *args, **kwargs):
        data = []
        for r in relationships:
            r_dict = dict(r)
            r_dict["start_hash"] = hash(getattr(r, "start", 0))
            r_dict["end_hash"] = hash(getattr(r, "end", 0))
            data.append(r_dict)

        super().__init__(data=data, *args, **kwargs)

        self.relationships = relationships
        self.start_nodes = [r.start for r in relationships]
        self.end_nodes = [r.end for r in relationships]

    def to_df(self):
        return pd.DataFrame([dict(x) for x in self.relationships])

    def expand(self):
        """
        Method takes the nodes that are multi-indexed in Relationships and expands
        out the properties in each of them, for a dataframe with the full set of
        all details on the entity-relationship pairs.
        """
        sn = NodeFrame(self.start_nodes)
        en = NodeFrame(self.end_nodes)
        r_cols = [x for x in self.columns if x not in ["start_hash", "end_hash"]]
        s_cols = [x for x in sn.columns if x not in ["hash_val"]]
        e_cols = [x for x in en.columns if x not in ["hash_val"]]
        col = r_cols + s_cols + e_cols
        src = (
            ["relationship"] * len(r_cols)
            + ["start"] * len(s_cols)
            + ["end"] * (len(e_cols))
        )
        exdf_col = pd.MultiIndex.from_arrays([src, col])
        exdf = (
            pd.merge(
                self.set_index("start_hash"),
                sn.set_index("hash_val"),
                right_index=True,
                left_index=True,
                suffixes=("_rel", "_start"),
            )
            .set_index("end_hash")
            .merge(
                en.set_index("hash_val"),
                right_index=True,
                left_index=True,
                suffixes=("_start", "_end"),
            )
            .reset_index(drop=True)
        )
        exdf.columns = exdf_col

        return exdf

    def invert(self, label="label"):
        """
        Examines the entities and relationships available based on entity type or
        another field
        """
        pass
