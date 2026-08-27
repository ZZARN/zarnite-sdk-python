# zarnite.AnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_performance_v1_analytics_agent_agent_id_performance_get**](AnalyticsApi.md#agent_performance_v1_analytics_agent_agent_id_performance_get) | **GET** /v1/analytics/agent/{agent_id}/performance | Agent Performance
[**org_overview_v1_analytics_org_org_id_get**](AnalyticsApi.md#org_overview_v1_analytics_org_org_id_get) | **GET** /v1/analytics/org/{org_id} | Org Overview
[**user_summary_v1_analytics_user_user_id_get**](AnalyticsApi.md#user_summary_v1_analytics_user_user_id_get) | **GET** /v1/analytics/user/{user_id} | User Summary
[**user_topics_v1_analytics_user_user_id_topics_get**](AnalyticsApi.md#user_topics_v1_analytics_user_user_id_topics_get) | **GET** /v1/analytics/user/{user_id}/topics | User Topics
[**user_trends_v1_analytics_user_user_id_trends_get**](AnalyticsApi.md#user_trends_v1_analytics_user_user_id_trends_get) | **GET** /v1/analytics/user/{user_id}/trends | User Trends


# **agent_performance_v1_analytics_agent_agent_id_performance_get**
> EnvelopeAgentPerformanceResponse agent_performance_v1_analytics_agent_agent_id_performance_get(agent_id, org_id)

Agent Performance

Get agent performance metrics.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_agent_performance_response import EnvelopeAgentPerformanceResponse
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
    api_instance = zarnite.AnalyticsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | 

    try:
        # Agent Performance
        api_response = api_instance.agent_performance_v1_analytics_agent_agent_id_performance_get(agent_id, org_id)
        print("The response of AnalyticsApi->agent_performance_v1_analytics_agent_agent_id_performance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->agent_performance_v1_analytics_agent_agent_id_performance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**|  | 

### Return type

[**EnvelopeAgentPerformanceResponse**](EnvelopeAgentPerformanceResponse.md)

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

# **org_overview_v1_analytics_org_org_id_get**
> EnvelopeOrgOverviewResponse org_overview_v1_analytics_org_org_id_get(org_id)

Org Overview

Get organization overview.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_org_overview_response import EnvelopeOrgOverviewResponse
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
    api_instance = zarnite.AnalyticsApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Org Overview
        api_response = api_instance.org_overview_v1_analytics_org_org_id_get(org_id)
        print("The response of AnalyticsApi->org_overview_v1_analytics_org_org_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->org_overview_v1_analytics_org_org_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**EnvelopeOrgOverviewResponse**](EnvelopeOrgOverviewResponse.md)

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

# **user_summary_v1_analytics_user_user_id_get**
> EnvelopeUserSummaryResponse user_summary_v1_analytics_user_user_id_get(user_id, org_id, agent_id)

User Summary

Get user activity summary.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_user_summary_response import EnvelopeUserSummaryResponse
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
    api_instance = zarnite.AnalyticsApi(api_client)
    user_id = 'user_id_example' # str | 
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str | 

    try:
        # User Summary
        api_response = api_instance.user_summary_v1_analytics_user_user_id_get(user_id, org_id, agent_id)
        print("The response of AnalyticsApi->user_summary_v1_analytics_user_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->user_summary_v1_analytics_user_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | 

### Return type

[**EnvelopeUserSummaryResponse**](EnvelopeUserSummaryResponse.md)

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

# **user_topics_v1_analytics_user_user_id_topics_get**
> EnvelopeUserTopicsResponse user_topics_v1_analytics_user_user_id_topics_get(user_id, org_id, agent_id, limit=limit)

User Topics

Get user conversation topics.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_user_topics_response import EnvelopeUserTopicsResponse
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
    api_instance = zarnite.AnalyticsApi(api_client)
    user_id = 'user_id_example' # str | 
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str | 
    limit = 10 # int |  (optional) (default to 10)

    try:
        # User Topics
        api_response = api_instance.user_topics_v1_analytics_user_user_id_topics_get(user_id, org_id, agent_id, limit=limit)
        print("The response of AnalyticsApi->user_topics_v1_analytics_user_user_id_topics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->user_topics_v1_analytics_user_user_id_topics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**EnvelopeUserTopicsResponse**](EnvelopeUserTopicsResponse.md)

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

# **user_trends_v1_analytics_user_user_id_trends_get**
> EnvelopeUsageTrendsResponse user_trends_v1_analytics_user_user_id_trends_get(user_id, org_id, agent_id, days=days)

User Trends

Get user usage trends over a given period.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_usage_trends_response import EnvelopeUsageTrendsResponse
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
    api_instance = zarnite.AnalyticsApi(api_client)
    user_id = 'user_id_example' # str | 
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str | 
    days = 30 # int |  (optional) (default to 30)

    try:
        # User Trends
        api_response = api_instance.user_trends_v1_analytics_user_user_id_trends_get(user_id, org_id, agent_id, days=days)
        print("The response of AnalyticsApi->user_trends_v1_analytics_user_user_id_trends_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->user_trends_v1_analytics_user_user_id_trends_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | 
 **days** | **int**|  | [optional] [default to 30]

### Return type

[**EnvelopeUsageTrendsResponse**](EnvelopeUsageTrendsResponse.md)

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

