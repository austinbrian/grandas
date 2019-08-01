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

    def __repr__(self):
        return f"(Node: {self._attrs})"

    def __setitem__(self, item: str, val):
        self._attrs[item] = val

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id

    def keys(self):
        return list(self._attrs.keys())
        # yield from iter(self._attrs.keys())

    def values(self):
        yield from iter(self._attrs.values())

    def items(self):
        yield from iter(self._attrs.items())


class Relationship:
    # NOTE: bidirectected relationships are duplicated as two relationships
    pass


class Subgraph:
    pass
