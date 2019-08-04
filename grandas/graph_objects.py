import json


class GOBase:
    """Base object for graph_object methods"""

    def __init__(self, **kwargs):
        self._attrs = dict(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.id = hash(self)

    def __getitem__(self, item: str):
        return self._attrs[item]

    def to_json(self) -> str:
        return json.dumps(self._attrs)

    def __repr__(self):
        return f"({self.__class__.__name__}: {self._attrs})"

    def __setitem__(self, item: str, val):
        self._attrs[item] = val

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id

    def __str__(self):
        return str(list(self._attrs.items()))

    def __hash__(self):
        return hash(str(self))

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
        yield from iter(self._attrs)


class Node(GOBase):
    """
    Nodes are created by passing in a dictionary or JSON object at initialization
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def link(self, **kwargs):
        """Create a relationship linkage between two Node objects"""
        return Relationship(start=self, **kwargs)


class Relationship(GOBase):
    # NOTE: bidirectected relationships are duplicated as two relationships
    def __init__(self, start=None, end=None, **kwargs):
        super().__init__(**kwargs)
        # if either of these is none, we're going to rename the other to the same node
        if not start:
            start = end
        if not end:
            end = start
        if not start:
            raise TypeError("missing required argument 'start'.")
        if not end:
            raise TypeError("missing required argument 'end'.")
        self.start = start
        self.end = end

    def __repr__(self):
        start_node = self.start
        end_node = self.end

        return f"{repr(self.start)}-\n({self.__class__.__name__}: {self._attrs}->\n{repr(self.end)}"


class Subgraph:
    pass
