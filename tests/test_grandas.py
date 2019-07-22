#!bin/bash/env python

import pytest
from grandas import graph_engine
from grandas import GraphFrame


def test_graph_engine_failure():
    with pytest.raises(Exception):
        graph_engine(engine='anything_but_neo4j')

def test_graph_frame():
    gf = GraphFrame()
    assert gf.a =='Hello test goodbye'
