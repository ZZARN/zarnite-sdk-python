# zarnite.MemoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memory_search_v1_memory_search_post**](MemoryApi.md#memory_search_v1_memory_search_post) | **POST** /v1/memory/search | Memory Search
[**memory_stats_v1_memory_stats_get**](MemoryApi.md#memory_stats_v1_memory_stats_get) | **GET** /v1/memory/stats | Memory Stats


# **memory_search_v1_memory_search_post**
> EnvelopeMemorySearchResponse memory_search_v1_memory_search_post(memory_search_request)

Memory Search

Search KB and memory for a query.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_memory_search_response import EnvelopeMemorySearchResponse
from zarnite.models.memory_search_request import MemorySearchRequest
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
    api_instance = zarnite.MemoryApi(api_client)
    memory_search_request = zarnite.MemorySearchRequest() # MemorySearchRequest | 

    try:
        # Memory Search
        api_response = api_instance.memory_search_v1_memory_search_post(memory_search_request)
        print("The response of MemoryApi->memory_search_v1_memory_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_search_v1_memory_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_search_request** | [**MemorySearchRequest**](MemorySearchRequest.md)|  | 

### Return type

[**EnvelopeMemorySearchResponse**](EnvelopeMemorySearchResponse.md)

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

# **memory_stats_v1_memory_stats_get**
> EnvelopeMemoryStatsResponse memory_stats_v1_memory_stats_get(org_id, agent_id)

Memory Stats

Get document counts for KB and memory collections.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_memory_stats_response import EnvelopeMemoryStatsResponse
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
    api_instance = zarnite.MemoryApi(api_client)
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str | 

    try:
        # Memory Stats
        api_response = api_instance.memory_stats_v1_memory_stats_get(org_id, agent_id)
        print("The response of MemoryApi->memory_stats_v1_memory_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->memory_stats_v1_memory_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | 

### Return type

[**EnvelopeMemoryStatsResponse**](EnvelopeMemoryStatsResponse.md)

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

