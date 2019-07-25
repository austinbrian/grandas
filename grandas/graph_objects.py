import json


class Node:
    """
    Nodes are created by passing in a dictionary or JSON object at initialization
    """

    def __init__(self, **kwargs):
        self._attrs = dict(**kwargs)

    def __getitem__(self, item: str):
        return self._attrs[item]

    def to_json(self) -> str:
        return json.dumps(self._attrs)


class Relationship:
    # NOTE: bidirectected relationships are duplicated as two relationships
    pass


class Subgraph:
    pass
