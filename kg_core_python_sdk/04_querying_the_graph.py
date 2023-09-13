# How to query the graph
# example: Fetching a subset of dataset version information incl. dependencies on authors

from kg_core.kg import kg

# initializing the KG client (for more options, see "initializing_the_kg_client.py")
kg_client = kg().build()

# Whilst listing instances of the KG or by fetching them by ids, you're only reading atomic entities and
# it would be required to manually resolve the dependencies by the sequential resolution of the contained references.
# Luckily, the EBRAINS KG also contains a query mechanism to traverse the graph in a single step:


# *************************************************************
# Using a dynamic query
# *************************************************************

# To specify a query for the KG, you can do so with the following structure. Please note
# that for your convenience, you have the KG Query Builder available at https://query.kg.ebrains.eu
query = {
  "@context": {
    "@vocab": "https://core.kg.ebrains.eu/vocab/query/",
    "query": "https://schema.hbp.eu/myQuery/",
    "propertyName": {
      "@id": "propertyName",
      "@type": "@id"
    },
    "path": {
      "@id": "path",
      "@type": "@id"
    }
  },
  "meta": {
    "type": "https://openminds.ebrains.eu/core/DatasetVersion",  # Defines the type to be queried
    "responseVocab": "https://schema.hbp.eu/myQuery/" # Specifies which "vocab" is supposed to be applied to the result (to reduce the semantic overhead)
  },
  "structure": [
    {
      "path": "@id", # Pick the "@id" attribute of the instance and ...
      "propertyName": "query:id" # ... rename it to this propertyName
    },
    {
      "propertyName": "query:fullName",
      "path": "https://openminds.ebrains.eu/vocab/fullName"
    },
    {
      "propertyName": "query:author",
      "path": "https://openminds.ebrains.eu/vocab/author",
      "ensureOrder": True, # Make sure the original insertion order is kept - please note, that this is not the case by default for performance reasons
      "structure": [ # The above mentioned path is a reference to another instance which is why we have to define a substructure of items we would like to return
        {
          "propertyName": "query:familyName",
          "path": "https://openminds.ebrains.eu/vocab/familyName"
        },
        {
          "propertyName": "query:givenName",
          "path": "https://openminds.ebrains.eu/vocab/givenName"
        }
      ]
    }
  ]
}

# The query can then be executed
query_result = kg_client.queries.test_query(query)

# And its results can be iterated just the same way as for the "listing" part
for item in query_result.items():
    print(item)

# Please also note, that with the "propertyName", a rename of the property is applied.
# In combination with the "responseVocab", the structure of the payload gets reduced (the semantic full key is reduced)
