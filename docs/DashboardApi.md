# zarnite.DashboardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get**](DashboardApi.md#learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get) | **GET** /v1/dashboard/organizations/{org_id}/learners/{learner_id}/insights | Learner Insights
[**organization_activity_v1_dashboard_organizations_org_id_activity_get**](DashboardApi.md#organization_activity_v1_dashboard_organizations_org_id_activity_get) | **GET** /v1/dashboard/organizations/{org_id}/activity | Organization Activity
[**organization_analytics_v1_dashboard_organizations_org_id_analytics_get**](DashboardApi.md#organization_analytics_v1_dashboard_organizations_org_id_analytics_get) | **GET** /v1/dashboard/organizations/{org_id}/analytics | Organization Analytics
[**organization_overview_v1_dashboard_organizations_org_id_overview_get**](DashboardApi.md#organization_overview_v1_dashboard_organizations_org_id_overview_get) | **GET** /v1/dashboard/organizations/{org_id}/overview | Organization Overview


# **learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get**
> EnvelopeLearnerInsightsResponse learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get(org_id, learner_id)

Learner Insights

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_insights_response import EnvelopeLearnerInsightsResponse
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
    api_instance = zarnite.DashboardApi(api_client)
    org_id = 'org_id_example' # str | 
    learner_id = 'learner_id_example' # str | 

    try:
        # Learner Insights
        api_response = api_instance.learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get(org_id, learner_id)
        print("The response of DashboardApi->learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->learner_insights_v1_dashboard_organizations_org_id_learners_learner_id_insights_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **learner_id** | **str**|  | 

### Return type

[**EnvelopeLearnerInsightsResponse**](EnvelopeLearnerInsightsResponse.md)

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

# **organization_activity_v1_dashboard_organizations_org_id_activity_get**
> EnvelopeActivityFeedResponse organization_activity_v1_dashboard_organizations_org_id_activity_get(org_id, limit=limit)

Organization Activity

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_activity_feed_response import EnvelopeActivityFeedResponse
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
    api_instance = zarnite.DashboardApi(api_client)
    org_id = 'org_id_example' # str | 
    limit = 20 # int |  (optional) (default to 20)

    try:
        # Organization Activity
        api_response = api_instance.organization_activity_v1_dashboard_organizations_org_id_activity_get(org_id, limit=limit)
        print("The response of DashboardApi->organization_activity_v1_dashboard_organizations_org_id_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->organization_activity_v1_dashboard_organizations_org_id_activity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**EnvelopeActivityFeedResponse**](EnvelopeActivityFeedResponse.md)

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

# **organization_analytics_v1_dashboard_organizations_org_id_analytics_get**
> EnvelopeOrganizationAnalyticsResponse organization_analytics_v1_dashboard_organizations_org_id_analytics_get(org_id, range=range, view=view, class_id=class_id, agent_id=agent_id, learner_id=learner_id)

Organization Analytics

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_organization_analytics_response import EnvelopeOrganizationAnalyticsResponse
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
    api_instance = zarnite.DashboardApi(api_client)
    org_id = 'org_id_example' # str | 
    range = 'Last 30 Days' # str |  (optional) (default to 'Last 30 Days')
    view = 'institution' # str |  (optional) (default to 'institution')
    class_id = 'class_id_example' # str |  (optional)
    agent_id = 'agent_id_example' # str |  (optional)
    learner_id = 'learner_id_example' # str |  (optional)

    try:
        # Organization Analytics
        api_response = api_instance.organization_analytics_v1_dashboard_organizations_org_id_analytics_get(org_id, range=range, view=view, class_id=class_id, agent_id=agent_id, learner_id=learner_id)
        print("The response of DashboardApi->organization_analytics_v1_dashboard_organizations_org_id_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->organization_analytics_v1_dashboard_organizations_org_id_analytics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **range** | **str**|  | [optional] [default to &#39;Last 30 Days&#39;]
 **view** | **str**|  | [optional] [default to &#39;institution&#39;]
 **class_id** | **str**|  | [optional] 
 **agent_id** | **str**|  | [optional] 
 **learner_id** | **str**|  | [optional] 

### Return type

[**EnvelopeOrganizationAnalyticsResponse**](EnvelopeOrganizationAnalyticsResponse.md)

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

# **organization_overview_v1_dashboard_organizations_org_id_overview_get**
> EnvelopeDashboardOverviewResponse organization_overview_v1_dashboard_organizations_org_id_overview_get(org_id)

Organization Overview

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_dashboard_overview_response import EnvelopeDashboardOverviewResponse
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
    api_instance = zarnite.DashboardApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Organization Overview
        api_response = api_instance.organization_overview_v1_dashboard_organizations_org_id_overview_get(org_id)
        print("The response of DashboardApi->organization_overview_v1_dashboard_organizations_org_id_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->organization_overview_v1_dashboard_organizations_org_id_overview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**EnvelopeDashboardOverviewResponse**](EnvelopeDashboardOverviewResponse.md)

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

