#!bin/bash/env python

import pytest
import pandas as pd
import json

from grandas import graph_engine
from grandas import GraphFrame, NodeFrame, RelationshipFrame
from grandas import Node, Relationship, Subgraph


def test_graph_engine_failure():
    with pytest.raises(Exception):
        graph_engine(engine="anything_but_neo4j")


@pytest.fixture
def generate_nodes():
    nodes = [
        {"label": "MAN", "name": "Adam", "ribs": 23, "id": "101"},
        {"label": "WOMAN", "name": "Eve", "ribs": 24, "id": "102"},
    ]
    return nodes


@pytest.fixture
def generate_relationships():
    relationships = [
        dict(zip(("start", "end", "label", "day"), ("101", "102", "gave_rib", "8")))
    ]
    return relationships


def test_graph_frame(generate_nodes, generate_relationships):
    nodes, relationships = generate_nodes, generate_relationships
    gf = GraphFrame(nodes=nodes)
    assert gf.a == "Hello test goodbye"
    assert type(gf.nodes) == NodeFrame


def test_node_creation(generate_nodes):
    nodes = [Node(**x) for x in generate_nodes]
    assert len(nodes) == len(generate_nodes)
    assert nodes[0]["label"] == "MAN"
    # assert str(nodes[0].to_json()) == str(dict(generate_nodes[0]))
    assert list(nodes[0].keys()) == list(generate_nodes[0].keys())
    node_to_series = pd.Series(data=nodes[0]._attrs)
    assert node_to_series["label"] == "MAN"


def test_nodes(generate_nodes):
    nodes = [Node(**x) for x in generate_nodes]
    assert len(nodes) == 2
    for n in nodes:
        assert len(n.keys()) == 4
    ndf = NodeFrame(nodes=nodes)
    assert ndf.shape == (2, 4)


def test_relationships(generate_relationships):
    rels = generate_relationships
    relationship_objects = [Relationship(**r) for r in rels]
    for e, r in enumerate(relationship_objects):
        assert dict(r) == rels[e]
