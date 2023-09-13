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

# result objects are paginated; default pagination size is 50
species = set()
count = 0
while result:
    print(f"result page: {count} - {count + result.size} of {result.total}")
    count += result.size
    if result.data:
        for i in result.data:
            if f"{openminds_prefix}species" in i:
                species.add(i[f"{openminds_prefix}species"]["@id"])
    result = result.next_page()
print()

# the Subject property 'species' can be of type (simple) Species or Strain
# a Strain instance again defines its (simple) Species type (linked through property 'species')
# linked instances can be retrieved in a cascading manner
species = list(species)
simple_species = set()
for s in species:
    species_uuid = os.path.basename(s)
    species_instance = kg_client.instances.get_by_id(species_uuid).data
    species_type = os.path.basename(species_instance["@type"][0])
    if species_type == "Species":
        simple_species.add(species_instance[f"{openminds_prefix}name"])
    elif species_type == "Strain":
        species_uuid = os.path.basename(species_instance[f"{openminds_prefix}species"]["@id"])
        simple_species_instance = kg_client.instances.get_by_id(species_uuid).data
        simple_species.add(simple_species_instance[f"{openminds_prefix}name"])
    else:
        print("UNKNOWN SPECIES TYPE")

print("Simple species names of Subjects registered in the KG:\n", "\n".join(sorted([f"\t{s}" for s in simple_species])))