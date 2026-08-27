# zarnite.LearnersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post**](LearnersApi.md#cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post) | **POST** /v1/learners/{learner_id}/cancel-deletion | Cancel Learner Deletion
[**create_learner_v1_learners_post**](LearnersApi.md#create_learner_v1_learners_post) | **POST** /v1/learners/ | Create Learner
[**deactivate_learner_v1_learners_learner_id_deactivate_post**](LearnersApi.md#deactivate_learner_v1_learners_learner_id_deactivate_post) | **POST** /v1/learners/{learner_id}/deactivate | Deactivate Learner
[**delete_learner_v1_learners_learner_id_delete**](LearnersApi.md#delete_learner_v1_learners_learner_id_delete) | **DELETE** /v1/learners/{learner_id} | Delete Learner
[**get_learner_v1_learners_learner_id_get**](LearnersApi.md#get_learner_v1_learners_learner_id_get) | **GET** /v1/learners/{learner_id} | Get Learner
[**learner_activity_v1_learners_learner_id_activity_get**](LearnersApi.md#learner_activity_v1_learners_learner_id_activity_get) | **GET** /v1/learners/{learner_id}/activity | Learner Activity
[**learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get**](LearnersApi.md#learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get) | **GET** /v1/learners/{learner_id}/longitudinal-feedback | Learner Longitudinal Feedback
[**learner_metadata_v1_learners_learner_id_metadata_get**](LearnersApi.md#learner_metadata_v1_learners_learner_id_metadata_get) | **GET** /v1/learners/{learner_id}/metadata | Learner Metadata
[**learner_score_v1_learners_learner_id_score_get**](LearnersApi.md#learner_score_v1_learners_learner_id_score_get) | **GET** /v1/learners/{learner_id}/score | Learner Score
[**learner_stats_v1_learners_learner_id_stats_get**](LearnersApi.md#learner_stats_v1_learners_learner_id_stats_get) | **GET** /v1/learners/{learner_id}/stats | Learner Stats
[**learner_summary_v1_learners_learner_id_summary_get**](LearnersApi.md#learner_summary_v1_learners_learner_id_summary_get) | **GET** /v1/learners/{learner_id}/summary | Learner Summary
[**list_learners_v1_learners_get**](LearnersApi.md#list_learners_v1_learners_get) | **GET** /v1/learners/ | List Learners
[**reinitiate_learner_v1_learners_learner_id_reinitiate_post**](LearnersApi.md#reinitiate_learner_v1_learners_learner_id_reinitiate_post) | **POST** /v1/learners/{learner_id}/reinitiate | Reinitiate Learner
[**schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post**](LearnersApi.md#schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post) | **POST** /v1/learners/{learner_id}/schedule-deletion | Schedule Learner Deletion
[**upload_csv_v1_learners_upload_csv_post**](LearnersApi.md#upload_csv_v1_learners_upload_csv_post) | **POST** /v1/learners/upload-csv | Upload Csv
[**verify_learner_v1_learners_verify_post**](LearnersApi.md#verify_learner_v1_learners_verify_post) | **POST** /v1/learners/verify | Verify Learner


# **cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post**
> EnvelopeLearnerDeletionScheduleResponse cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post(learner_id, org_id)

Cancel Learner Deletion

Cancel a pending learner deletion request.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_deletion_schedule_response import EnvelopeLearnerDeletionScheduleResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Cancel Learner Deletion
        api_response = api_instance.cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post(learner_id, org_id)
        print("The response of LearnersApi->cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->cancel_learner_deletion_v1_learners_learner_id_cancel_deletion_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerDeletionScheduleResponse**](EnvelopeLearnerDeletionScheduleResponse.md)

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

# **create_learner_v1_learners_post**
> EnvelopeLearnerCreateResponse create_learner_v1_learners_post(learner_create)

Create Learner

Create a new learner, generate an access key, and email credentials.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_create_response import EnvelopeLearnerCreateResponse
from zarnite.models.learner_create import LearnerCreate
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_create = zarnite.LearnerCreate() # LearnerCreate | 

    try:
        # Create Learner
        api_response = api_instance.create_learner_v1_learners_post(learner_create)
        print("The response of LearnersApi->create_learner_v1_learners_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->create_learner_v1_learners_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_create** | [**LearnerCreate**](LearnerCreate.md)|  | 

### Return type

[**EnvelopeLearnerCreateResponse**](EnvelopeLearnerCreateResponse.md)

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

# **deactivate_learner_v1_learners_learner_id_deactivate_post**
> EnvelopeLearnerDeactivateResponse deactivate_learner_v1_learners_learner_id_deactivate_post(learner_id, org_id)

Deactivate Learner

Deactivate a learner: set status to inactive and revoke their access key.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_deactivate_response import EnvelopeLearnerDeactivateResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Deactivate Learner
        api_response = api_instance.deactivate_learner_v1_learners_learner_id_deactivate_post(learner_id, org_id)
        print("The response of LearnersApi->deactivate_learner_v1_learners_learner_id_deactivate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->deactivate_learner_v1_learners_learner_id_deactivate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerDeactivateResponse**](EnvelopeLearnerDeactivateResponse.md)

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

# **delete_learner_v1_learners_learner_id_delete**
> EnvelopeLearnerDeleteResponse delete_learner_v1_learners_learner_id_delete(learner_id, org_id)

Delete Learner

Delete a learner and learner-scoped records immediately.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_delete_response import EnvelopeLearnerDeleteResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Delete Learner
        api_response = api_instance.delete_learner_v1_learners_learner_id_delete(learner_id, org_id)
        print("The response of LearnersApi->delete_learner_v1_learners_learner_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->delete_learner_v1_learners_learner_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerDeleteResponse**](EnvelopeLearnerDeleteResponse.md)

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

# **get_learner_v1_learners_learner_id_get**
> EnvelopeLearnerResponse get_learner_v1_learners_learner_id_get(learner_id, org_id)

Get Learner

Get a single learner by ID.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_response import EnvelopeLearnerResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Get Learner
        api_response = api_instance.get_learner_v1_learners_learner_id_get(learner_id, org_id)
        print("The response of LearnersApi->get_learner_v1_learners_learner_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->get_learner_v1_learners_learner_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerResponse**](EnvelopeLearnerResponse.md)

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

# **learner_activity_v1_learners_learner_id_activity_get**
> EnvelopeLearnerActivityResponse learner_activity_v1_learners_learner_id_activity_get(learner_id, org_id, limit=limit)

Learner Activity

Get recent session activity timeline for a learner.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_activity_response import EnvelopeLearnerActivityResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope
    limit = 20 # int | Max events to return (optional) (default to 20)

    try:
        # Learner Activity
        api_response = api_instance.learner_activity_v1_learners_learner_id_activity_get(learner_id, org_id, limit=limit)
        print("The response of LearnersApi->learner_activity_v1_learners_learner_id_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->learner_activity_v1_learners_learner_id_activity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 
 **limit** | **int**| Max events to return | [optional] [default to 20]

### Return type

[**EnvelopeLearnerActivityResponse**](EnvelopeLearnerActivityResponse.md)

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

# **learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get**
> EnvelopeLearnerLongitudinalFeedbackResponse learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get(learner_id, org_id, limit=limit)

Learner Longitudinal Feedback

Get concise feedback comparing the learner's latest sessions with prior ones.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_longitudinal_feedback_response import EnvelopeLearnerLongitudinalFeedbackResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope
    limit = 5 # int | Recent conversation count to analyze (optional) (default to 5)

    try:
        # Learner Longitudinal Feedback
        api_response = api_instance.learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get(learner_id, org_id, limit=limit)
        print("The response of LearnersApi->learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->learner_longitudinal_feedback_v1_learners_learner_id_longitudinal_feedback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 
 **limit** | **int**| Recent conversation count to analyze | [optional] [default to 5]

### Return type

[**EnvelopeLearnerLongitudinalFeedbackResponse**](EnvelopeLearnerLongitudinalFeedbackResponse.md)

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

# **learner_metadata_v1_learners_learner_id_metadata_get**
> EnvelopeLearnerMetadataResponse learner_metadata_v1_learners_learner_id_metadata_get(learner_id, org_id, activity_limit=activity_limit)

Learner Metadata

Return safe learner metadata plus current learning context in one frontend-friendly call.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_metadata_response import EnvelopeLearnerMetadataResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope
    activity_limit = 5 # int | Recent activity items to include (optional) (default to 5)

    try:
        # Learner Metadata
        api_response = api_instance.learner_metadata_v1_learners_learner_id_metadata_get(learner_id, org_id, activity_limit=activity_limit)
        print("The response of LearnersApi->learner_metadata_v1_learners_learner_id_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->learner_metadata_v1_learners_learner_id_metadata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 
 **activity_limit** | **int**| Recent activity items to include | [optional] [default to 5]

### Return type

[**EnvelopeLearnerMetadataResponse**](EnvelopeLearnerMetadataResponse.md)

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

# **learner_score_v1_learners_learner_id_score_get**
> EnvelopeLearnerScoreResponse learner_score_v1_learners_learner_id_score_get(learner_id, org_id)

Learner Score

Compute CEFR progression score for a learner.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_score_response import EnvelopeLearnerScoreResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Learner Score
        api_response = api_instance.learner_score_v1_learners_learner_id_score_get(learner_id, org_id)
        print("The response of LearnersApi->learner_score_v1_learners_learner_id_score_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->learner_score_v1_learners_learner_id_score_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerScoreResponse**](EnvelopeLearnerScoreResponse.md)

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

# **learner_stats_v1_learners_learner_id_stats_get**
> EnvelopeLearnerStatsResponse learner_stats_v1_learners_learner_id_stats_get(learner_id, org_id)

Learner Stats

Get aggregated session & usage stats for a learner.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_stats_response import EnvelopeLearnerStatsResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Learner Stats
        api_response = api_instance.learner_stats_v1_learners_learner_id_stats_get(learner_id, org_id)
        print("The response of LearnersApi->learner_stats_v1_learners_learner_id_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->learner_stats_v1_learners_learner_id_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerStatsResponse**](EnvelopeLearnerStatsResponse.md)

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

# **learner_summary_v1_learners_learner_id_summary_get**
> EnvelopeLearnerSummaryResponse learner_summary_v1_learners_learner_id_summary_get(learner_id, org_id)

Learner Summary

Get personalized welcome message and summary for a learner.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_summary_response import EnvelopeLearnerSummaryResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Learner Summary
        api_response = api_instance.learner_summary_v1_learners_learner_id_summary_get(learner_id, org_id)
        print("The response of LearnersApi->learner_summary_v1_learners_learner_id_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->learner_summary_v1_learners_learner_id_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerSummaryResponse**](EnvelopeLearnerSummaryResponse.md)

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

# **list_learners_v1_learners_get**
> EnvelopeListLearnerResponse list_learners_v1_learners_get(org_id, status=status, limit=limit, offset=offset)

List Learners

List learners for an organization.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_learner_response import EnvelopeListLearnerResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    org_id = 'org_id_example' # str | Organization scope
    status = 'status_example' # str | Filter by status (optional)
    limit = 50 # int | Page size (optional) (default to 50)
    offset = 0 # int | Page offset (optional) (default to 0)

    try:
        # List Learners
        api_response = api_instance.list_learners_v1_learners_get(org_id, status=status, limit=limit, offset=offset)
        print("The response of LearnersApi->list_learners_v1_learners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->list_learners_v1_learners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization scope | 
 **status** | **str**| Filter by status | [optional] 
 **limit** | **int**| Page size | [optional] [default to 50]
 **offset** | **int**| Page offset | [optional] [default to 0]

### Return type

[**EnvelopeListLearnerResponse**](EnvelopeListLearnerResponse.md)

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

# **reinitiate_learner_v1_learners_learner_id_reinitiate_post**
> EnvelopeLearnerReinitiateResponse reinitiate_learner_v1_learners_learner_id_reinitiate_post(learner_id, org_id)

Reinitiate Learner

Reinitiate a learner: revoke old key, generate new key, set status to active, re-send credentials email.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_reinitiate_response import EnvelopeLearnerReinitiateResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Reinitiate Learner
        api_response = api_instance.reinitiate_learner_v1_learners_learner_id_reinitiate_post(learner_id, org_id)
        print("The response of LearnersApi->reinitiate_learner_v1_learners_learner_id_reinitiate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->reinitiate_learner_v1_learners_learner_id_reinitiate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerReinitiateResponse**](EnvelopeLearnerReinitiateResponse.md)

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

# **schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post**
> EnvelopeLearnerDeletionScheduleResponse schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post(learner_id, org_id)

Schedule Learner Deletion

Schedule learner data deletion to execute after the retention window.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_deletion_schedule_response import EnvelopeLearnerDeletionScheduleResponse
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_id = 'learner_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Schedule Learner Deletion
        api_response = api_instance.schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post(learner_id, org_id)
        print("The response of LearnersApi->schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->schedule_learner_deletion_v1_learners_learner_id_schedule_deletion_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeLearnerDeletionScheduleResponse**](EnvelopeLearnerDeletionScheduleResponse.md)

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

# **upload_csv_v1_learners_upload_csv_post**
> EnvelopeLearnerCsvResult upload_csv_v1_learners_upload_csv_post(org_id, file)

Upload Csv

Bulk import learners from CSV. Expected columns: name, email, learner_id (optional).

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_csv_result import EnvelopeLearnerCsvResult
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
    api_instance = zarnite.LearnersApi(api_client)
    org_id = 'org_id_example' # str | Organization scope
    file = None # bytes | 

    try:
        # Upload Csv
        api_response = api_instance.upload_csv_v1_learners_upload_csv_post(org_id, file)
        print("The response of LearnersApi->upload_csv_v1_learners_upload_csv_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->upload_csv_v1_learners_upload_csv_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization scope | 
 **file** | **bytes**|  | 

### Return type

[**EnvelopeLearnerCsvResult**](EnvelopeLearnerCsvResult.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_learner_v1_learners_verify_post**
> EnvelopeLearnerVerifyResponse verify_learner_v1_learners_verify_post(learner_verify_request)

Verify Learner

Verify a learner-id + access key pair.

Returns valid=true and the learner status if the key matches, valid=false otherwise.
Never reveals whether the learner exists to prevent enumeration.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_learner_verify_response import EnvelopeLearnerVerifyResponse
from zarnite.models.learner_verify_request import LearnerVerifyRequest
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
    api_instance = zarnite.LearnersApi(api_client)
    learner_verify_request = zarnite.LearnerVerifyRequest() # LearnerVerifyRequest | 

    try:
        # Verify Learner
        api_response = api_instance.verify_learner_v1_learners_verify_post(learner_verify_request)
        print("The response of LearnersApi->verify_learner_v1_learners_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LearnersApi->verify_learner_v1_learners_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learner_verify_request** | [**LearnerVerifyRequest**](LearnerVerifyRequest.md)|  | 

### Return type

[**EnvelopeLearnerVerifyResponse**](EnvelopeLearnerVerifyResponse.md)

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

