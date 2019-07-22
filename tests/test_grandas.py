#!bin/bash/env python

import pytest
from grandas import graph_engine


def test_graph_engine_failure():
    with pytest.raises(Exception):
        graph_engine(engine='anything_but_neo4j')
