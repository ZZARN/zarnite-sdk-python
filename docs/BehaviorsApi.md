# zarnite.BehaviorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_behavior_v1_behaviors_post**](BehaviorsApi.md#create_behavior_v1_behaviors_post) | **POST** /v1/behaviors/ | Create Behavior
[**delete_behavior_v1_behaviors_behavior_id_delete**](BehaviorsApi.md#delete_behavior_v1_behaviors_behavior_id_delete) | **DELETE** /v1/behaviors/{behavior_id} | Delete Behavior
[**get_behavior_v1_behaviors_behavior_id_get**](BehaviorsApi.md#get_behavior_v1_behaviors_behavior_id_get) | **GET** /v1/behaviors/{behavior_id} | Get Behavior
[**list_behaviors_v1_behaviors_get**](BehaviorsApi.md#list_behaviors_v1_behaviors_get) | **GET** /v1/behaviors/ | List Behaviors
[**update_behavior_v1_behaviors_behavior_id_patch**](BehaviorsApi.md#update_behavior_v1_behaviors_behavior_id_patch) | **PATCH** /v1/behaviors/{behavior_id} | Update Behavior
[**update_behavior_v1_behaviors_behavior_id_put**](BehaviorsApi.md#update_behavior_v1_behaviors_behavior_id_put) | **PUT** /v1/behaviors/{behavior_id} | Update Behavior


# **create_behavior_v1_behaviors_post**
> EnvelopeBehaviorResponse create_behavior_v1_behaviors_post(behavior_create)

Create Behavior

Create a new behavior config.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.behavior_create import BehaviorCreate
from zarnite.models.envelope_behavior_response import EnvelopeBehaviorResponse
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
    api_instance = zarnite.BehaviorsApi(api_client)
    behavior_create = zarnite.BehaviorCreate() # BehaviorCreate | 

    try:
        # Create Behavior
        api_response = api_instance.create_behavior_v1_behaviors_post(behavior_create)
        print("The response of BehaviorsApi->create_behavior_v1_behaviors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorsApi->create_behavior_v1_behaviors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_create** | [**BehaviorCreate**](BehaviorCreate.md)|  | 

### Return type

[**EnvelopeBehaviorResponse**](EnvelopeBehaviorResponse.md)

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

# **delete_behavior_v1_behaviors_behavior_id_delete**
> EnvelopeBehaviorDeleteResponse delete_behavior_v1_behaviors_behavior_id_delete(behavior_id, org_id)

Delete Behavior

Delete a behavior. Linked agents will have behavior_id set to NULL.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_behavior_delete_response import EnvelopeBehaviorDeleteResponse
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
    api_instance = zarnite.BehaviorsApi(api_client)
    behavior_id = 'behavior_id_example' # str | 
    org_id = 'org_id_example' # str | 

    try:
        # Delete Behavior
        api_response = api_instance.delete_behavior_v1_behaviors_behavior_id_delete(behavior_id, org_id)
        print("The response of BehaviorsApi->delete_behavior_v1_behaviors_behavior_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorsApi->delete_behavior_v1_behaviors_behavior_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**|  | 
 **org_id** | **str**|  | 

### Return type

[**EnvelopeBehaviorDeleteResponse**](EnvelopeBehaviorDeleteResponse.md)

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

# **get_behavior_v1_behaviors_behavior_id_get**
> EnvelopeBehaviorResponse get_behavior_v1_behaviors_behavior_id_get(behavior_id, org_id)

Get Behavior

Get a specific behavior config.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_behavior_response import EnvelopeBehaviorResponse
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
    api_instance = zarnite.BehaviorsApi(api_client)
    behavior_id = 'behavior_id_example' # str | 
    org_id = 'org_id_example' # str | 

    try:
        # Get Behavior
        api_response = api_instance.get_behavior_v1_behaviors_behavior_id_get(behavior_id, org_id)
        print("The response of BehaviorsApi->get_behavior_v1_behaviors_behavior_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorsApi->get_behavior_v1_behaviors_behavior_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**|  | 
 **org_id** | **str**|  | 

### Return type

[**EnvelopeBehaviorResponse**](EnvelopeBehaviorResponse.md)

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

# **list_behaviors_v1_behaviors_get**
> EnvelopeListBehaviorResponse list_behaviors_v1_behaviors_get(org_id, limit=limit, offset=offset)

List Behaviors

List all behaviors for an organization.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_behavior_response import EnvelopeListBehaviorResponse
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
    api_instance = zarnite.BehaviorsApi(api_client)
    org_id = 'org_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Behaviors
        api_response = api_instance.list_behaviors_v1_behaviors_get(org_id, limit=limit, offset=offset)
        print("The response of BehaviorsApi->list_behaviors_v1_behaviors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorsApi->list_behaviors_v1_behaviors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**EnvelopeListBehaviorResponse**](EnvelopeListBehaviorResponse.md)

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

# **update_behavior_v1_behaviors_behavior_id_patch**
> EnvelopeBehaviorResponse update_behavior_v1_behaviors_behavior_id_patch(behavior_id, org_id, behavior_update)

Update Behavior

Update an existing behavior config.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.behavior_update import BehaviorUpdate
from zarnite.models.envelope_behavior_response import EnvelopeBehaviorResponse
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
    api_instance = zarnite.BehaviorsApi(api_client)
    behavior_id = 'behavior_id_example' # str | 
    org_id = 'org_id_example' # str | 
    behavior_update = zarnite.BehaviorUpdate() # BehaviorUpdate | 

    try:
        # Update Behavior
        api_response = api_instance.update_behavior_v1_behaviors_behavior_id_patch(behavior_id, org_id, behavior_update)
        print("The response of BehaviorsApi->update_behavior_v1_behaviors_behavior_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorsApi->update_behavior_v1_behaviors_behavior_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**|  | 
 **org_id** | **str**|  | 
 **behavior_update** | [**BehaviorUpdate**](BehaviorUpdate.md)|  | 

### Return type

[**EnvelopeBehaviorResponse**](EnvelopeBehaviorResponse.md)

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

# **update_behavior_v1_behaviors_behavior_id_put**
> EnvelopeBehaviorResponse update_behavior_v1_behaviors_behavior_id_put(behavior_id, org_id, behavior_update)

Update Behavior

Update an existing behavior config.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.behavior_update import BehaviorUpdate
from zarnite.models.envelope_behavior_response import EnvelopeBehaviorResponse
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
    api_instance = zarnite.BehaviorsApi(api_client)
    behavior_id = 'behavior_id_example' # str | 
    org_id = 'org_id_example' # str | 
    behavior_update = zarnite.BehaviorUpdate() # BehaviorUpdate | 

    try:
        # Update Behavior
        api_response = api_instance.update_behavior_v1_behaviors_behavior_id_put(behavior_id, org_id, behavior_update)
        print("The response of BehaviorsApi->update_behavior_v1_behaviors_behavior_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BehaviorsApi->update_behavior_v1_behaviors_behavior_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **behavior_id** | **str**|  | 
 **org_id** | **str**|  | 
 **behavior_update** | [**BehaviorUpdate**](BehaviorUpdate.md)|  | 

### Return type

[**EnvelopeBehaviorResponse**](EnvelopeBehaviorResponse.md)

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

