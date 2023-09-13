# manipulating an instance
# example: Person instance

from uuid import uuid4

from kg_core.kg import kg

# initializing the KG client (for more options, see "initializing_the_kg_client.py")
kg_client = kg().build()

# First, we create an instance - e.g. a representation of ourself:

person = {
    "@type": "https://openminds.ebrains.eu/core/Person",
    "https://openminds.ebrains.eu/vocab/givenName": "YOUR_GIVEN_NAME",
    "https://openminds.ebrains.eu/vocab/familyName": "YOUR_FAMILY_NAME"
}

space = "myspace" # Instances in the KG live in so-called "spaces" for which you can have different access rights. One space you always have write access to is "myspace"


# You have two options to create the instance: Either you let the system assign an ID for your instance...
creation_result = kg_client.instances.create_new(person, space)

# ... or you define it yourself. In the latter case, you're responsible to provide a unique identifier (UUID) - if duplicates are detected, the system will throw an error
our_uuid = uuid4()
creation_result = kg_client.instances.create_new_with_id(person, our_uuid, space)

instance_id = creation_result.data.uuid # The response will contain the UUID of the instance (either assigned by the system or returning the UUID you have defined yourself)


# Manipulating an instance

# You now can manipulate the existing instance. This can be done in two different ways: Full replacement or partial update.

# Full update
full_update = {
    "@type": "https://openminds.ebrains.eu/core/Person",
    "https://openminds.ebrains.eu/vocab/givenName": "YOUR_NEW_GIVEN_NAME"
}

result = kg_client.instances.contribute_to_full_replacement(full_update, instance_id)
print(result.data) # Because we did a full update, the given name of the person is updated and the "familyName" is gone (because we didn't provide any)


partial_update = {
    "https://openminds.ebrains.eu/vocab/familyName": "YOUR_NEW_FAMILY_NAME"
}

result = kg_client.instances.contribute_to_partial_replacement(partial_update, instance_id)
print(result.data) # The instance now contains the already existing givenName as well as the new familyName because we did a partial update and just "added" something. Please note, that by defining a new value for an existing property would replace it

# Why is this called "contribute"?
# In the above example, you're the only contributor to the instance which means that all that counts is what you define.
# However, in other cases, multiple contributors (e.g. other users, automation scripts, etc.) to the same instance can add information to the entity.
# In this case, the resulting entity is a result out of what you contribute as well as what others contribute - and you're therefore not replacing the entity but rather your contribution to the entity.

# But how to remove a value of another contributor you're asking? By explicitly setting it to null:

partial_update = {
    "https://openminds.ebrains.eu/vocab/familyName": None
}
result = kg_client.instances.contribute_to_partial_replacement(partial_update, instance_id)


# How to create a reference to another instance?

# The EBRAINS KG uses JSON-LD as its structure. This means that references are - according to the standard - defined as

reference = {
    "https://someReferenceProperty": {
        "@id": "http://some/identifier/of/the/referenced/property"
    }
}

# A speciality of the EBRAINS KG is that it can handle multiple identifiers and does lazy resolution - this means
# you can use any value for the reference which is either the UUID as defined in KG or any value specified in the "http://schema.org/identiier" property of an entity.
# This means, you can add any (external) identifier to an instance by simply adding it to the "http://schema.org/identifier" property and you can reference it from any other element.
# Lazy resolution means that the referenced instance doesn't need to exist in the system at the moment of ingestion. Once an instance is added / the identifier is added to an existing instance,
# the system will automatically resolve the previously defined reference. This allows you to upload your instance in any order.
