# EBRAINS Data Handling

This repository holds a collection of code examples that demonstrate how to handle data managed in the EBRAINS Knowledge Graph (KG) using:  
- **KG Core Python SDK**   
- **fairgraph**  

Additional tools that are going to be helpful for handling data are:   
- **KG Search**  
- **KG QueryBuilder**  
- **openMINDS**  
- **ebrains-drive**  

## Basic knowledge

The **EBRAINS Knowledge Graph** is a data management system with a graph database at it's core. A graph database is composed of nodes which store metadata in form of property-value pairs, and edges which define the relationship between nodes. Each node in a graph database receives a unique identifier and can be individually referenced. Data are typically described by the metadata of a multiple nodes and edges and different data can share the same nodes, building a searchable network.

Graph databases are schema-less, meaning nodes and edges do not have to be constraint. This makes graph databases highly flexible and explicitly suitable for heterogenous data collections. However, to optimise the ability to query data in the graph database, the registration of nodes and edges have to be harmonised (constraint). For this purpose, the EBRAINS Knowledge Graph adopted the **openMINDS metadata framework**. The framework provides metadata models which are composed of interlinked metadata schemas that define the type of possible nodes, the content of a specfic node according to it's type, and the possible edges between the nodes within a graph database.

Besides the graph database, the EBRAINS Knowledge Graph system includes supportive tooling or services for data registration, curation management, publication management, query building, automation environments, and statistics. Nearly all application programming interface (API) endpoints of the EBRAINS Knowledge Graph system require the authentication of a requesting user. For the EBRAINS Knowledge Graph system, the authorization of a user to read and/or write depends on the user's role. Within the graph database, roles can be defined globally, for publication stages (released vs in-progress), for specific virtual spaces, or for individual nodes.
