# single instance handling
# example: Person instance

import os
import json
from kg_core.kg import kg
from kg_core.request import ExtendedResponseConfiguration, Pagination

# initializing the KG client
kg_client = kg().build()

# retrieving an instance using its universally unique identifier (uuid)
instance_uuid = "5bc17d5c-f5a2-4350-be30-8515da2e4e37"
instance = kg_client.instances.get_by_id(instance_uuid).data
print()

# instances are formatted as JSONLDs and contain structured metadata (key-value pairs) for a certain concept/entity
# the concept/entity of an instance is provided in the @type
# the @type also defines the schema that was used as template to create the instance
# a schema type is composed of the openMINDS metadata model prefix and a name
print("@type:", instance["@type"][0])
print("@type - name:", os.path.basename(instance["@type"][0]))
print("@type - openminds prefix:", os.path.dirname(instance["@type"][0]))
print()

# an instance also receives a universally unique identifier (uuid) which is provided in the @id
# the @id is composed of the actual uuid and a KG system prefix for instances
print("@id:", instance["@id"])
print("@id - uuid:", os.path.basename(instance["@id"]))
print("@id - KG instance prefix:", os.path.dirname(instance["@id"]))
print()

# for all key-value pairs defined by the metadata model, the key starts with a openMINDS vocabulary prefix
openminds_prefix = "https://openminds.ebrains.eu/vocab/"
openminds_metadata = {k: instance[k] for k in instance.keys() if k.startswith(openminds_prefix)}
for key, value in sorted(openminds_metadata.items()):
    print(f"{key}:", value)
print()

# for all key-value pairs additionally defined by the KG system, the key starts with another prefix
kg_metadata = {k: instance[k] for k in instance.keys() if not k.startswith(openminds_prefix) and not k.startswith("@")}
for key, value in sorted(kg_metadata.items()):
    print(f"{key}:", value)
print()

# embedded instances (for embedded schema types)
for key, value in sorted(openminds_metadata.items()):
    if isinstance(value, dict) and "@type" in value.keys():
        print(key)
        print(json.dumps(value, sort_keys=True, indent=2))
    elif isinstance(value, list) and all(isinstance(i, dict) for i in value) and all("@type" in i.keys() for i in value):
        print(key)
        print(json.dumps(value, sort_keys=True, indent=2))


# resolving edges (links to other instances)
# TODO

