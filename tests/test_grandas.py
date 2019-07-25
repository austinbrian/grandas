#!bin/bash/env python

import pytest
import pandas as pd
from grandas import graph_engine
from grandas import GraphFrame
from grandas import Node, Relationship, Subgraph


def test_graph_engine_failure():
    with pytest.raises(Exception):
        graph_engine(engine="anything_but_neo4j")


@pytest.fixture
def generate_nodes():
    nodes = [
        {"label": "MAN", "name": "Adam", "id": "101"},
        {"label": "WOMAN", "name": "Eve", "id": "102"},
    ]
    return nodes


@pytest.fixture
def generate_relationships():
    relationships = [
        dict(zip(("source", "target", "label", "day"), ("101", "102", "gave_rib", "8")))
    ]
    return relationships


def test_graph_frame(generate_nodes, generate_relationships):
    nodes, relationships = generate_nodes, generate_relationships
    gf = GraphFrame(nodes=nodes)
    assert gf.a == "Hello test goodbye"
    assert type(gf.nodes) == pd.Series


def test_node_creation(generate_nodes):
    print(generate_nodes)
    nodes = [Node(**x) for x in generate_nodes]
    print(nodes[0]._attrs)
    assert nodes[0]["label"] == "MAN"
    assert nodes[0].to_json() == '{"label": "MAN", "name": "Adam", "id": "101"}'
