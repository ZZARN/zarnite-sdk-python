# zarnite.APIKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_stats_v1_api_keys_stats_get**](APIKeysApi.md#api_key_stats_v1_api_keys_stats_get) | **GET** /v1/api-keys/stats | Api Key Stats
[**create_api_key_v1_api_keys_post**](APIKeysApi.md#create_api_key_v1_api_keys_post) | **POST** /v1/api-keys/ | Create Api Key
[**list_api_keys_v1_api_keys_get**](APIKeysApi.md#list_api_keys_v1_api_keys_get) | **GET** /v1/api-keys/ | List Api Keys
[**revoke_api_key_v1_api_keys_key_id_delete**](APIKeysApi.md#revoke_api_key_v1_api_keys_key_id_delete) | **DELETE** /v1/api-keys/{key_id} | Revoke Api Key
[**update_api_key_v1_api_keys_key_id_put**](APIKeysApi.md#update_api_key_v1_api_keys_key_id_put) | **PUT** /v1/api-keys/{key_id} | Update Api Key


# **api_key_stats_v1_api_keys_stats_get**
> EnvelopeApiKeyStatsResponse api_key_stats_v1_api_keys_stats_get(org_id)

Api Key Stats

Aggregate API key statistics for the org.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_api_key_stats_response import EnvelopeApiKeyStatsResponse
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
    api_instance = zarnite.APIKeysApi(api_client)
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Api Key Stats
        api_response = api_instance.api_key_stats_v1_api_keys_stats_get(org_id)
        print("The response of APIKeysApi->api_key_stats_v1_api_keys_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->api_key_stats_v1_api_keys_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeApiKeyStatsResponse**](EnvelopeApiKeyStatsResponse.md)

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

# **create_api_key_v1_api_keys_post**
> EnvelopeApiKeyCreateResponse create_api_key_v1_api_keys_post(api_key_create)

Create Api Key

Create a new API key. Returns the raw key exactly once.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.api_key_create import ApiKeyCreate
from zarnite.models.envelope_api_key_create_response import EnvelopeApiKeyCreateResponse
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
    api_instance = zarnite.APIKeysApi(api_client)
    api_key_create = zarnite.ApiKeyCreate() # ApiKeyCreate | 

    try:
        # Create Api Key
        api_response = api_instance.create_api_key_v1_api_keys_post(api_key_create)
        print("The response of APIKeysApi->create_api_key_v1_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->create_api_key_v1_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create** | [**ApiKeyCreate**](ApiKeyCreate.md)|  | 

### Return type

[**EnvelopeApiKeyCreateResponse**](EnvelopeApiKeyCreateResponse.md)

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

# **list_api_keys_v1_api_keys_get**
> EnvelopeListApiKeyResponse list_api_keys_v1_api_keys_get(org_id)

List Api Keys

List all API keys for an org (never returns raw keys).

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_api_key_response import EnvelopeListApiKeyResponse
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
    api_instance = zarnite.APIKeysApi(api_client)
    org_id = 'org_id_example' # str | Organization scope

    try:
        # List Api Keys
        api_response = api_instance.list_api_keys_v1_api_keys_get(org_id)
        print("The response of APIKeysApi->list_api_keys_v1_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->list_api_keys_v1_api_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeListApiKeyResponse**](EnvelopeListApiKeyResponse.md)

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

# **revoke_api_key_v1_api_keys_key_id_delete**
> EnvelopeApiKeyDeleteResponse revoke_api_key_v1_api_keys_key_id_delete(key_id, org_id)

Revoke Api Key

Permanently revoke (delete) an API key.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_api_key_delete_response import EnvelopeApiKeyDeleteResponse
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
    api_instance = zarnite.APIKeysApi(api_client)
    key_id = 'key_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Revoke Api Key
        api_response = api_instance.revoke_api_key_v1_api_keys_key_id_delete(key_id, org_id)
        print("The response of APIKeysApi->revoke_api_key_v1_api_keys_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->revoke_api_key_v1_api_keys_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeApiKeyDeleteResponse**](EnvelopeApiKeyDeleteResponse.md)

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

# **update_api_key_v1_api_keys_key_id_put**
> EnvelopeApiKeyResponse update_api_key_v1_api_keys_key_id_put(key_id, org_id, api_key_update)

Update Api Key

Update API key metadata (name, scopes, rate_limit, is_active).

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.api_key_update import ApiKeyUpdate
from zarnite.models.envelope_api_key_response import EnvelopeApiKeyResponse
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
    api_instance = zarnite.APIKeysApi(api_client)
    key_id = 'key_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope
    api_key_update = zarnite.ApiKeyUpdate() # ApiKeyUpdate | 

    try:
        # Update Api Key
        api_response = api_instance.update_api_key_v1_api_keys_key_id_put(key_id, org_id, api_key_update)
        print("The response of APIKeysApi->update_api_key_v1_api_keys_key_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->update_api_key_v1_api_keys_key_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 
 **api_key_update** | [**ApiKeyUpdate**](ApiKeyUpdate.md)|  | 

### Return type

[**EnvelopeApiKeyResponse**](EnvelopeApiKeyResponse.md)

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

