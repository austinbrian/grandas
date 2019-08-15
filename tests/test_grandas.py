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
def generate_node_dict():
    nodes = [
        {"label": "MAN", "name": "Adam", "ribs": 23, "id": "101"},
        {"label": "WOMAN", "name": "Eve", "ribs": 24, "id": "102"},
    ]
    return nodes

@pytest.fixture
def generate_nodes(generate_node_dict):
    nodes = [Node(**x) for x in generate_node_dict]
    return nodes

@pytest.fixture
def generate_nodeframe(generate_nodes):
    return NodeFrame(nodes=generate_nodes)

@pytest.fixture
def generate_relationships_dict():
    relationships = [
        dict(zip(("start", "end", "label", "day"), ("101", "102", "gave_rib", "8")))
    ]
    return relationships

@pytest.fixture
def generate_relationships(generate_relationships_dict):
    rels = [Relationship(**x) for x in generate_relationships_dict]
    return rels


def test_relationships(generate_relationships):
    rels = generate_relationships
    r, *others = rels
    assert r.start=='101'
    assert r.end=='102'

@pytest.fixture
def generate_relationshipframe(generate_relationships):
    return RelationshipFrame(nodes=generate_nodes)

@pytest.mark.skip
def test_graph_frame(generate_nodes, generate_relationships):
    nodes, relationships = generate_nodes, generate_relationships
    nodes = [Node(**x) for x in generate_nodes]
    relationships = [Relationship(**x) for x in generate_relationships]
    gf = GraphFrame(nodes=nodes, relationships=relationships)
    assert gf.a == "Hello test goodbye"
    assert type(gf.nodes) == NodeFrame


def test_node_creation(generate_nodes):
    nodes = [Node(**x) for x in generate_nodes]
    assert len(nodes) == len(generate_nodes)
    assert nodes[0]["label"] == "MAN"
    assert list(nodes[0].keys()) == list(generate_nodes[0].keys())
    node_to_series = pd.Series(data=nodes[0]._attrs)
    assert node_to_series["label"] == "MAN"


def test_nodes(generate_node_dict):
    nodes = [Node(**x) for x in generate_node_dict]
    assert len(nodes) == 2
    for n in nodes:
        assert len(n.keys()) == 4
    ndf = NodeFrame(nodes=nodes)
    # need to add one for the hash_value column
    assert ndf.shape == (2, 5)


