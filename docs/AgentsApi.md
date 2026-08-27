# zarnite.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_learner_v1_agents_agent_id_assignments_post**](AgentsApi.md#assign_learner_v1_agents_agent_id_assignments_post) | **POST** /v1/agents/{agent_id}/assignments | Assign Learner
[**create_agent_v1_agents_post**](AgentsApi.md#create_agent_v1_agents_post) | **POST** /v1/agents/ | Create Agent
[**delete_agent_v1_agents_agent_id_delete**](AgentsApi.md#delete_agent_v1_agents_agent_id_delete) | **DELETE** /v1/agents/{agent_id} | Delete Agent
[**get_agent_v1_agents_agent_id_get**](AgentsApi.md#get_agent_v1_agents_agent_id_get) | **GET** /v1/agents/{agent_id} | Get Agent
[**list_agents_v1_agents_get**](AgentsApi.md#list_agents_v1_agents_get) | **GET** /v1/agents/ | List Agents
[**list_assignments_v1_agents_agent_id_assignments_get**](AgentsApi.md#list_assignments_v1_agents_agent_id_assignments_get) | **GET** /v1/agents/{agent_id}/assignments | List Assignments
[**revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete**](AgentsApi.md#revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete) | **DELETE** /v1/agents/{agent_id}/assignments/{learner_id} | Revoke Assignment
[**update_agent_v1_agents_agent_id_patch**](AgentsApi.md#update_agent_v1_agents_agent_id_patch) | **PATCH** /v1/agents/{agent_id} | Update Agent
[**update_agent_v1_agents_agent_id_put**](AgentsApi.md#update_agent_v1_agents_agent_id_put) | **PUT** /v1/agents/{agent_id} | Update Agent


# **assign_learner_v1_agents_agent_id_assignments_post**
> EnvelopeAssignmentResponse assign_learner_v1_agents_agent_id_assignments_post(agent_id, assignment_create)

Assign Learner

Assign a learner to this agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.assignment_create import AssignmentCreate
from zarnite.models.envelope_assignment_response import EnvelopeAssignmentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    assignment_create = zarnite.AssignmentCreate() # AssignmentCreate | 

    try:
        # Assign Learner
        api_response = api_instance.assign_learner_v1_agents_agent_id_assignments_post(agent_id, assignment_create)
        print("The response of AgentsApi->assign_learner_v1_agents_agent_id_assignments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->assign_learner_v1_agents_agent_id_assignments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **assignment_create** | [**AssignmentCreate**](AssignmentCreate.md)|  | 

### Return type

[**EnvelopeAssignmentResponse**](EnvelopeAssignmentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_v1_agents_post**
> EnvelopeAgentResponse create_agent_v1_agents_post(agent_create)

Create Agent

Create a new agent. Requires admin role.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.agent_create import AgentCreate
from zarnite.models.envelope_agent_response import EnvelopeAgentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_create = zarnite.AgentCreate() # AgentCreate | 

    try:
        # Create Agent
        api_response = api_instance.create_agent_v1_agents_post(agent_create)
        print("The response of AgentsApi->create_agent_v1_agents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_v1_agents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_create** | [**AgentCreate**](AgentCreate.md)|  | 

### Return type

[**EnvelopeAgentResponse**](EnvelopeAgentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_v1_agents_agent_id_delete**
> EnvelopeAgentDeleteResponse delete_agent_v1_agents_agent_id_delete(agent_id, org_id)

Delete Agent

Delete an agent and return a typed confirmation envelope.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_agent_delete_response import EnvelopeAgentDeleteResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | 

    try:
        # Delete Agent
        api_response = api_instance.delete_agent_v1_agents_agent_id_delete(agent_id, org_id)
        print("The response of AgentsApi->delete_agent_v1_agents_agent_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_agent_v1_agents_agent_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**|  | 

### Return type

[**EnvelopeAgentDeleteResponse**](EnvelopeAgentDeleteResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_v1_agents_agent_id_get**
> EnvelopeAgentResponse get_agent_v1_agents_agent_id_get(agent_id, org_id)

Get Agent

Get details of a specific agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_agent_response import EnvelopeAgentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | 

    try:
        # Get Agent
        api_response = api_instance.get_agent_v1_agents_agent_id_get(agent_id, org_id)
        print("The response of AgentsApi->get_agent_v1_agents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_v1_agents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**|  | 

### Return type

[**EnvelopeAgentResponse**](EnvelopeAgentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agents_v1_agents_get**
> EnvelopeListAgentResponse list_agents_v1_agents_get(org_id, agent_id=agent_id, status=status, limit=limit, offset=offset)

List Agents

List all agents for an organization.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_agent_response import EnvelopeListAgentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Agents
        api_response = api_instance.list_agents_v1_agents_get(org_id, agent_id=agent_id, status=status, limit=limit, offset=offset)
        print("The response of AgentsApi->list_agents_v1_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agents_v1_agents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**EnvelopeListAgentResponse**](EnvelopeListAgentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments_v1_agents_agent_id_assignments_get**
> EnvelopeListAssignmentResponse list_assignments_v1_agents_agent_id_assignments_get(agent_id, org_id)

List Assignments

List learners assigned to this agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_assignment_response import EnvelopeListAssignmentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # List Assignments
        api_response = api_instance.list_assignments_v1_agents_agent_id_assignments_get(agent_id, org_id)
        print("The response of AgentsApi->list_assignments_v1_agents_agent_id_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_assignments_v1_agents_agent_id_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeListAssignmentResponse**](EnvelopeListAssignmentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete**
> EnvelopeAssignmentDeleteResponse revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete(agent_id, learner_id, org_id)

Revoke Assignment

Revoke a learner's assignment from this agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_assignment_delete_response import EnvelopeAssignmentDeleteResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Revoke Assignment
        api_response = api_instance.revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete(agent_id, learner_id, org_id)
        print("The response of AgentsApi->revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->revoke_assignment_v1_agents_agent_id_assignments_learner_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeAssignmentDeleteResponse**](EnvelopeAssignmentDeleteResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_v1_agents_agent_id_patch**
> EnvelopeAgentResponse update_agent_v1_agents_agent_id_patch(agent_id, org_id, agent_update)

Update Agent

Update an existing agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.agent_update import AgentUpdate
from zarnite.models.envelope_agent_response import EnvelopeAgentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | 
    agent_update = zarnite.AgentUpdate() # AgentUpdate | 

    try:
        # Update Agent
        api_response = api_instance.update_agent_v1_agents_agent_id_patch(agent_id, org_id, agent_update)
        print("The response of AgentsApi->update_agent_v1_agents_agent_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_agent_v1_agents_agent_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**|  | 
 **agent_update** | [**AgentUpdate**](AgentUpdate.md)|  | 

### Return type

[**EnvelopeAgentResponse**](EnvelopeAgentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_v1_agents_agent_id_put**
> EnvelopeAgentResponse update_agent_v1_agents_agent_id_put(agent_id, org_id, agent_update)

Update Agent

Update an existing agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.agent_update import AgentUpdate
from zarnite.models.envelope_agent_response import EnvelopeAgentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = zarnite.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | 
    agent_update = zarnite.AgentUpdate() # AgentUpdate | 

    try:
        # Update Agent
        api_response = api_instance.update_agent_v1_agents_agent_id_put(agent_id, org_id, agent_update)
        print("The response of AgentsApi->update_agent_v1_agents_agent_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_agent_v1_agents_agent_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**|  | 
 **agent_update** | [**AgentUpdate**](AgentUpdate.md)|  | 

### Return type

[**EnvelopeAgentResponse**](EnvelopeAgentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

