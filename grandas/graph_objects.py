import json


class Node:
    """
    Nodes are created by passing in a dictionary or JSON object at initialization
    """

    def __init__(self, **kwargs):
        self._attrs = dict(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

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

    def _keys(self):
        yield from iter(self._attrs.keys())

    def keys(self):
        return list(self._keys())

    def _values(self):
        yield from iter(self._attrs.values())

    def values(self):
        return list(self._values())

    def items(self):
        yield from iter(self._attrs.items())

    def to_dict(self):
        return self._attrs

    def __iter__(self):
        yield from iter(self._attrs.items())


class Relationship:
    # NOTE: bidirectected relationships are duplicated as two relationships
    pass


class Subgraph:
    pass
