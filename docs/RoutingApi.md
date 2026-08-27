# zarnite.RoutingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_config_v1_routing_org_config_get**](RoutingApi.md#get_org_config_v1_routing_org_config_get) | **GET** /v1/routing/org-config | Get Org Config
[**get_user_category_v1_routing_user_category_get**](RoutingApi.md#get_user_category_v1_routing_user_category_get) | **GET** /v1/routing/user-category | Get User Category
[**update_org_config_v1_routing_org_config_put**](RoutingApi.md#update_org_config_v1_routing_org_config_put) | **PUT** /v1/routing/org-config | Update Org Config
[**update_user_category_v1_routing_user_category_put**](RoutingApi.md#update_user_category_v1_routing_user_category_put) | **PUT** /v1/routing/user-category | Update User Category


# **get_org_config_v1_routing_org_config_get**
> EnvelopeOrgRoutingConfigResponse get_org_config_v1_routing_org_config_get(org_id)

Get Org Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_routing_config_response import EnvelopeOrgRoutingConfigResponse
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
    api_instance = zarnite.RoutingApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Get Org Config
        api_response = api_instance.get_org_config_v1_routing_org_config_get(org_id)
        print("The response of RoutingApi->get_org_config_v1_routing_org_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->get_org_config_v1_routing_org_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**EnvelopeOrgRoutingConfigResponse**](EnvelopeOrgRoutingConfigResponse.md)

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

# **get_user_category_v1_routing_user_category_get**
> EnvelopeOrgUserCategoryResponse get_user_category_v1_routing_user_category_get(org_id, user_id)

Get User Category

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_user_category_response import EnvelopeOrgUserCategoryResponse
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
    api_instance = zarnite.RoutingApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Get User Category
        api_response = api_instance.get_user_category_v1_routing_user_category_get(org_id, user_id)
        print("The response of RoutingApi->get_user_category_v1_routing_user_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->get_user_category_v1_routing_user_category_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**EnvelopeOrgUserCategoryResponse**](EnvelopeOrgUserCategoryResponse.md)

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

# **update_org_config_v1_routing_org_config_put**
> EnvelopeOrgRoutingConfigResponse update_org_config_v1_routing_org_config_put(org_id, org_routing_config_update_request)

Update Org Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_routing_config_response import EnvelopeOrgRoutingConfigResponse
from zarnite.models.org_routing_config_update_request import OrgRoutingConfigUpdateRequest
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
    api_instance = zarnite.RoutingApi(api_client)
    org_id = 'org_id_example' # str | 
    org_routing_config_update_request = zarnite.OrgRoutingConfigUpdateRequest() # OrgRoutingConfigUpdateRequest | 

    try:
        # Update Org Config
        api_response = api_instance.update_org_config_v1_routing_org_config_put(org_id, org_routing_config_update_request)
        print("The response of RoutingApi->update_org_config_v1_routing_org_config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->update_org_config_v1_routing_org_config_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **org_routing_config_update_request** | [**OrgRoutingConfigUpdateRequest**](OrgRoutingConfigUpdateRequest.md)|  | 

### Return type

[**EnvelopeOrgRoutingConfigResponse**](EnvelopeOrgRoutingConfigResponse.md)

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

# **update_user_category_v1_routing_user_category_put**
> EnvelopeOrgUserCategoryResponse update_user_category_v1_routing_user_category_put(org_id, user_id, org_user_category_update_request)

Update User Category

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_user_category_response import EnvelopeOrgUserCategoryResponse
from zarnite.models.org_user_category_update_request import OrgUserCategoryUpdateRequest
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
    api_instance = zarnite.RoutingApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str | 
    org_user_category_update_request = zarnite.OrgUserCategoryUpdateRequest() # OrgUserCategoryUpdateRequest | 

    try:
        # Update User Category
        api_response = api_instance.update_user_category_v1_routing_user_category_put(org_id, user_id, org_user_category_update_request)
        print("The response of RoutingApi->update_user_category_v1_routing_user_category_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->update_user_category_v1_routing_user_category_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 
 **org_user_category_update_request** | [**OrgUserCategoryUpdateRequest**](OrgUserCategoryUpdateRequest.md)|  | 

### Return type

[**EnvelopeOrgUserCategoryResponse**](EnvelopeOrgUserCategoryResponse.md)

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

