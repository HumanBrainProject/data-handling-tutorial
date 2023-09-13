# How to list instances by type

from kg_core.kg import kg

# initializing the KG client (for more options, see "initializing_the_kg_client.py")
from kg_core.request import Pagination

kg_client = kg().build()

# You can list instances by their type:
type = "https://openminds.ebrains.eu/core/DatasetVersion"
instances_result = kg_client.instances.list(type)

# Please note that what you retrieve is a 'ResultPage'. This is, because the listing API is paginated and
# you might not want to list all instances (there can be a lot) but rather process them page by page.

# To iterate the list (and control the pagination), you have multiple options:

# Option 1:
# If you want to run through all instances, you can use the items() mechanism. Once the end of a page is reached, the library automatically fetches the next.
# Please note that only the current page is kept in memory -> this allows to keep the footprint low.

# Caveats: Please note that you shouldn't manipulate instances directly within the loop because it can cause unexpected states of the pagination.
for instance in instances_result.items():
    print(instance)

# Option 2:
# To have more control on what happens during the iteration (e.g. also keeping previous items in memory),
# You can make use of the "next_page()" mechanism. Please note that "next_page" returns None if you've reached
# end of the listing -> accordingly it is safe to use it for the termination condition of the while loop.

# If you just want to check if a next page exists but don't want to load it, you can also use the "has_next_page" method
instances = instances_result.data
while instances:
    for instance in instances:
        print(instance)
    instances = instances_result.next_page()

# Depending on the payload of the instances, it might be a good idea to adapt the page-size which defaults to 50
# (to either minimize the memory footprint or the number of roundtrips).
# This can be achieved by defining the pagination settings:

kg_client.instances.list(type, pagination=Pagination(size=100))