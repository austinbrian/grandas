
# Grandas
[![Build Status](https://travis-ci.com/austinbrian/grandas.svg?token=L6ySxzeSx54Es7V1pQTz&branch=master)](https://travis-ci.com/austinbrian/grandas)

Grandas as a library that allows simplified, flexible analysis of the nodes and relationships stored in a graph database. It allows a user to search for and filter information and connections contained in a subgraph of a graph database.

## Data Structures
### Node
A Node object is the basic entity object and identifies any noun in your graph dataset.


### Relationship
A Relationship stores the way that any two nodes in your dataset are related. Bi-directional relationships here are stored as two independent relationships.

### NodeFrame
Nodeframes allow users to see the nodes in their graph databases, and further enable them to filter and resolve redundant nodes.

### RelationshipFrame
The RelationshipFrame object stores a series of Relationship objects as a pandas DataFrame, using the hashed value of the full node to identify where the start and ending points for each relationship are.

### GraphFrame
A GraphFrame is comprised of a NodeFrame (attribute: `nodes`) and a RelationshipFrame (attribute: `rels`).

---
## Getting Started
To get started using grandas, you can install it using pip:
```
pip install grandas
```

From there, load in nodes and relationships to a GraphFrame object, similar to how you would use a pandas DataFrame.

```
import grandas as gd

nodes = [
  Node(label='PERSON',name='Alice',age='27'),
  Node(label='PERSON',name='Bob',age='24'),
  ]
alice, bob = nodes
rels = [
  Relationship(start=alice, end=bob, label='owes_money_to',amount=10)
]
gf = GraphFrame(nodes=nodes, relationships=rels)

node_frame = gf.nodes
relationship_frame =  gf.rels
```


---
## Contributing
Contributions are more than welcome! Please just submit a pull request to the `develop` branch.
