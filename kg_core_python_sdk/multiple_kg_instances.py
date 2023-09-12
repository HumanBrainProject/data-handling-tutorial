# multiple instance handling
# example: Subject instance

import os
import json
from kg_core.kg import kg
from kg_core.request import ExtendedResponseConfiguration, Pagination

# initializing the KG client
kg_client = kg().build()

# retrieving an instance using its universally unique identifier (uuid)
instance_type = "https://openminds.ebrains.eu/core/Subject"
result = kg_client.instances.list(instance_type)

# learning about result pages
print("Number of retrieved instances:", result.size)
print("Number of total instances:", result.total)
print("Time to retrieve instances:", f"{result.duration_in_ms} ms")
print("Error report:", result.error)
print()

# getting to the metadata of one instance in results
instance_data = result.data[0]
for key, value in sorted(instance_data.items()):
    print(f"{key}:", value)
print()

# predefine openminds_prefix
openminds_prefix = "https://openminds.ebrains.eu/vocab/"

# result objects are paginated; let's get all species
species = set()
while result.has_next_page():
    if result.data:
        for i in result.data:
            if f"{openminds_prefix}species" in i:
                species.add(i[f"{openminds_prefix}species"]["@id"])
    result = result.next_page()
print("Number of retrieved species:", len(species))

# retrieve simple species or strain label
# TODO