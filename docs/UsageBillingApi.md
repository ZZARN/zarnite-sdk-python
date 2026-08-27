# zarnite.UsageBillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_credits_v1_usage_credits_get**](UsageBillingApi.md#get_org_credits_v1_usage_credits_get) | **GET** /v1/usage/credits | Get Org Credits
[**get_org_rag_session_limit_v1_usage_rag_session_limit_get**](UsageBillingApi.md#get_org_rag_session_limit_v1_usage_rag_session_limit_get) | **GET** /v1/usage/rag-session-limit | Get Org Rag Session Limit
[**get_org_usage_v1_usage_get**](UsageBillingApi.md#get_org_usage_v1_usage_get) | **GET** /v1/usage/ | Get Org Usage
[**get_usage_logs_v1_usage_logs_get**](UsageBillingApi.md#get_usage_logs_v1_usage_logs_get) | **GET** /v1/usage/logs | Get Usage Logs
[**update_org_credits_v1_usage_credits_put**](UsageBillingApi.md#update_org_credits_v1_usage_credits_put) | **PUT** /v1/usage/credits | Update Org Credits
[**update_org_rag_session_limit_v1_usage_rag_session_limit_put**](UsageBillingApi.md#update_org_rag_session_limit_v1_usage_rag_session_limit_put) | **PUT** /v1/usage/rag-session-limit | Update Org Rag Session Limit


# **get_org_credits_v1_usage_credits_get**
> EnvelopeOrgCreditWalletResponse get_org_credits_v1_usage_credits_get(org_id)

Get Org Credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_credit_wallet_response import EnvelopeOrgCreditWalletResponse
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
    api_instance = zarnite.UsageBillingApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Get Org Credits
        api_response = api_instance.get_org_credits_v1_usage_credits_get(org_id)
        print("The response of UsageBillingApi->get_org_credits_v1_usage_credits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageBillingApi->get_org_credits_v1_usage_credits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**EnvelopeOrgCreditWalletResponse**](EnvelopeOrgCreditWalletResponse.md)

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

# **get_org_rag_session_limit_v1_usage_rag_session_limit_get**
> EnvelopeOrgRagSessionLimitResponse get_org_rag_session_limit_v1_usage_rag_session_limit_get(org_id, user_id=user_id)

Get Org Rag Session Limit

Get org-level monthly RAG session limit policy and current usage snapshot.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_rag_session_limit_response import EnvelopeOrgRagSessionLimitResponse
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
    api_instance = zarnite.UsageBillingApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Get Org Rag Session Limit
        api_response = api_instance.get_org_rag_session_limit_v1_usage_rag_session_limit_get(org_id, user_id=user_id)
        print("The response of UsageBillingApi->get_org_rag_session_limit_v1_usage_rag_session_limit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageBillingApi->get_org_rag_session_limit_v1_usage_rag_session_limit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**EnvelopeOrgRagSessionLimitResponse**](EnvelopeOrgRagSessionLimitResponse.md)

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

# **get_org_usage_v1_usage_get**
> EnvelopeAggregatedUsage get_org_usage_v1_usage_get(org_id, start_date=start_date, end_date=end_date)

Get Org Usage

Retrieve aggregated usage for an organization over a date range.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_aggregated_usage import EnvelopeAggregatedUsage
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
    api_instance = zarnite.UsageBillingApi(api_client)
    org_id = 'org_id_example' # str | 
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)

    try:
        # Get Org Usage
        api_response = api_instance.get_org_usage_v1_usage_get(org_id, start_date=start_date, end_date=end_date)
        print("The response of UsageBillingApi->get_org_usage_v1_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageBillingApi->get_org_usage_v1_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 

### Return type

[**EnvelopeAggregatedUsage**](EnvelopeAggregatedUsage.md)

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

# **get_usage_logs_v1_usage_logs_get**
> EnvelopeListUsageLogEntry get_usage_logs_v1_usage_logs_get(org_id, agent_id=agent_id, limit=limit, offset=offset)

Get Usage Logs

Retrieve raw usage logs.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_usage_log_entry import EnvelopeListUsageLogEntry
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
    api_instance = zarnite.UsageBillingApi(api_client)
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Usage Logs
        api_response = api_instance.get_usage_logs_v1_usage_logs_get(org_id, agent_id=agent_id, limit=limit, offset=offset)
        print("The response of UsageBillingApi->get_usage_logs_v1_usage_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageBillingApi->get_usage_logs_v1_usage_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**EnvelopeListUsageLogEntry**](EnvelopeListUsageLogEntry.md)

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

# **update_org_credits_v1_usage_credits_put**
> EnvelopeOrgCreditWalletResponse update_org_credits_v1_usage_credits_put(org_id, org_credit_wallet_update_request)

Update Org Credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_credit_wallet_response import EnvelopeOrgCreditWalletResponse
from zarnite.models.org_credit_wallet_update_request import OrgCreditWalletUpdateRequest
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
    api_instance = zarnite.UsageBillingApi(api_client)
    org_id = 'org_id_example' # str | 
    org_credit_wallet_update_request = zarnite.OrgCreditWalletUpdateRequest() # OrgCreditWalletUpdateRequest | 

    try:
        # Update Org Credits
        api_response = api_instance.update_org_credits_v1_usage_credits_put(org_id, org_credit_wallet_update_request)
        print("The response of UsageBillingApi->update_org_credits_v1_usage_credits_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageBillingApi->update_org_credits_v1_usage_credits_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **org_credit_wallet_update_request** | [**OrgCreditWalletUpdateRequest**](OrgCreditWalletUpdateRequest.md)|  | 

### Return type

[**EnvelopeOrgCreditWalletResponse**](EnvelopeOrgCreditWalletResponse.md)

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

# **update_org_rag_session_limit_v1_usage_rag_session_limit_put**
> EnvelopeOrgRagSessionLimitResponse update_org_rag_session_limit_v1_usage_rag_session_limit_put(org_id, org_rag_session_limit_update_request)

Update Org Rag Session Limit

Create/update org-level monthly RAG session restriction policy.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_rag_session_limit_response import EnvelopeOrgRagSessionLimitResponse
from zarnite.models.org_rag_session_limit_update_request import OrgRagSessionLimitUpdateRequest
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
    api_instance = zarnite.UsageBillingApi(api_client)
    org_id = 'org_id_example' # str | 
    org_rag_session_limit_update_request = zarnite.OrgRagSessionLimitUpdateRequest() # OrgRagSessionLimitUpdateRequest | 

    try:
        # Update Org Rag Session Limit
        api_response = api_instance.update_org_rag_session_limit_v1_usage_rag_session_limit_put(org_id, org_rag_session_limit_update_request)
        print("The response of UsageBillingApi->update_org_rag_session_limit_v1_usage_rag_session_limit_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageBillingApi->update_org_rag_session_limit_v1_usage_rag_session_limit_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **org_rag_session_limit_update_request** | [**OrgRagSessionLimitUpdateRequest**](OrgRagSessionLimitUpdateRequest.md)|  | 

### Return type

[**EnvelopeOrgRagSessionLimitResponse**](EnvelopeOrgRagSessionLimitResponse.md)

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

