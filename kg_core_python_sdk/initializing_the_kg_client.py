import os
import json
from kg_core.kg import kg
from kg_core.request import ExtendedResponseConfiguration, Pagination


# **************************************************************
# Basic initialization
# **************************************************************
# The KG library is set-up to work with minimal configuration wherever possible. This is achieved by
# default settings which cover the most probable settings. However, almost everything can be customized:

# To initialize the KG library, the convenience method
kg_client_builder = kg()
# can be used. This method returns a client builder to customize the configuration.
# By default, the kg library is configured to point to the public EBRAINS KG endpoint available at https://core.kg.ebrains.eu. This can be customized
kg_client_builder = kg(host="the.endpoint.of.your.own.kg")


# **************************************************************
# Authentication
# *************************************************************

# By default, the library uses the device flow to authenticate
# Context: This is useful for interactive scripts (somebody manually triggering a script and sitting in front of it). It requires minimal configuration.
kg_client_builder = kg()
# Alternatively, the device flow can also be explicitly stated (and - if needed - customized):
kg_client_builder = kg().with_device_flow()

# If the code is run in an already authenticated and you already have a valid access token, you can use
kg_client_builder = kg().with_token("YOUR_ACCESS_TOKEN")

# If you want to run scripts in a non-supervised way (e.g. as cron-jobs or server-2-server, you want to use a credential-based approach.
# For this, you require a service-account and can use the "with_credentials" mechanism. Please note, that the library will update the access token whenever needed
kg_client_builder = kg().with_credentials("you_client_id", "your_client_secret")

# If you have any other scenario (e.g. the script runs in a context where authentication is taken care of and you wnat to make sure, the access token is updated from the context - e.g. in a JupyterLab scenario),
# you can provide your custom provider:

kg_client_builder = kg().with_custom_token_provider(lambda: clb_oauth.get_token()) # an example using the JupyterLab mechanism to access the token of the current session


# *************************************************************
# Building your client
# *************************************************************

# Last but not least, there are two different clients you can build: The default client (suited for most users) and an admin client (to separate the administration API of the KG)
# In almost any case, what you're looking for is the default client providing you access to the standard functionalities:
kg_client = kg_client_builder.build()

# In case you really would want to use the administration APIs of KG, you can do so by using (obviously your user-account will need to have the appropriate rights to do so)
kg_client = kg_client_builder.build_admin()
