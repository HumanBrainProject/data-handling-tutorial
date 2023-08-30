# EBRAINS Data Handling

This repository holds a collection of code examples that demonstrate how to handle data managed in the EBRAINS Knowledge Graph using:
(1) KG Core Python SDK 
(2) fairgraph

## essential knowledge

The EBRAINS Knowledge Graph is a data management system with a graph database at it's core. A graph database is composed of nodes which store metadata in form of property-value pairs, and edges which define the relationship between nodes. Each node in a graph database receives a unique identifier and can be individually referenced. Data are typically described by the metadata of a multiple nodes and edges and data of different sources can share the same nodes, building a searchable graphical network.

Graph databases are schema-less, meaning nodes and edges do not have to be constraint. This makes graph databases highly flexible and explitly suitable for heterogenous data collections. However, to optimise the ability to query data, the registration of nodes and edges in the graph database have to be harmonised (constraint). For this purpose, the EBRAINS Knowledge Graph adopted the openMINDS metadata framework. 
