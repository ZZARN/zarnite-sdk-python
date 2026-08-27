# zarnite.VoiceRuntimeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap_session_v1_voice_runtime_sessions_bootstrap_post**](VoiceRuntimeApi.md#bootstrap_session_v1_voice_runtime_sessions_bootstrap_post) | **POST** /v1/voice-runtime/sessions/bootstrap | Bootstrap Session
[**close_session_v1_voice_runtime_sessions_session_id_close_post**](VoiceRuntimeApi.md#close_session_v1_voice_runtime_sessions_session_id_close_post) | **POST** /v1/voice-runtime/sessions/{session_id}/close | Close Session
[**write_feedback_v1_voice_runtime_sessions_session_id_feedback_post**](VoiceRuntimeApi.md#write_feedback_v1_voice_runtime_sessions_session_id_feedback_post) | **POST** /v1/voice-runtime/sessions/{session_id}/feedback | Write Feedback


# **bootstrap_session_v1_voice_runtime_sessions_bootstrap_post**
> EnvelopeVoiceRuntimeBootstrapResponse bootstrap_session_v1_voice_runtime_sessions_bootstrap_post(voice_runtime_bootstrap_request)

Bootstrap Session

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_voice_runtime_bootstrap_response import EnvelopeVoiceRuntimeBootstrapResponse
from zarnite.models.voice_runtime_bootstrap_request import VoiceRuntimeBootstrapRequest
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
    api_instance = zarnite.VoiceRuntimeApi(api_client)
    voice_runtime_bootstrap_request = zarnite.VoiceRuntimeBootstrapRequest() # VoiceRuntimeBootstrapRequest | 

    try:
        # Bootstrap Session
        api_response = api_instance.bootstrap_session_v1_voice_runtime_sessions_bootstrap_post(voice_runtime_bootstrap_request)
        print("The response of VoiceRuntimeApi->bootstrap_session_v1_voice_runtime_sessions_bootstrap_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoiceRuntimeApi->bootstrap_session_v1_voice_runtime_sessions_bootstrap_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_runtime_bootstrap_request** | [**VoiceRuntimeBootstrapRequest**](VoiceRuntimeBootstrapRequest.md)|  | 

### Return type

[**EnvelopeVoiceRuntimeBootstrapResponse**](EnvelopeVoiceRuntimeBootstrapResponse.md)

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

# **close_session_v1_voice_runtime_sessions_session_id_close_post**
> EnvelopeVoiceRuntimeCloseResponse close_session_v1_voice_runtime_sessions_session_id_close_post(session_id, voice_runtime_close_request)

Close Session

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_voice_runtime_close_response import EnvelopeVoiceRuntimeCloseResponse
from zarnite.models.voice_runtime_close_request import VoiceRuntimeCloseRequest
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
    api_instance = zarnite.VoiceRuntimeApi(api_client)
    session_id = 'session_id_example' # str | 
    voice_runtime_close_request = zarnite.VoiceRuntimeCloseRequest() # VoiceRuntimeCloseRequest | 

    try:
        # Close Session
        api_response = api_instance.close_session_v1_voice_runtime_sessions_session_id_close_post(session_id, voice_runtime_close_request)
        print("The response of VoiceRuntimeApi->close_session_v1_voice_runtime_sessions_session_id_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoiceRuntimeApi->close_session_v1_voice_runtime_sessions_session_id_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **voice_runtime_close_request** | [**VoiceRuntimeCloseRequest**](VoiceRuntimeCloseRequest.md)|  | 

### Return type

[**EnvelopeVoiceRuntimeCloseResponse**](EnvelopeVoiceRuntimeCloseResponse.md)

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

# **write_feedback_v1_voice_runtime_sessions_session_id_feedback_post**
> EnvelopeVoiceRuntimeFeedbackResponse write_feedback_v1_voice_runtime_sessions_session_id_feedback_post(session_id, voice_runtime_feedback_request)

Write Feedback

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_voice_runtime_feedback_response import EnvelopeVoiceRuntimeFeedbackResponse
from zarnite.models.voice_runtime_feedback_request import VoiceRuntimeFeedbackRequest
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
    api_instance = zarnite.VoiceRuntimeApi(api_client)
    session_id = 'session_id_example' # str | 
    voice_runtime_feedback_request = zarnite.VoiceRuntimeFeedbackRequest() # VoiceRuntimeFeedbackRequest | 

    try:
        # Write Feedback
        api_response = api_instance.write_feedback_v1_voice_runtime_sessions_session_id_feedback_post(session_id, voice_runtime_feedback_request)
        print("The response of VoiceRuntimeApi->write_feedback_v1_voice_runtime_sessions_session_id_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoiceRuntimeApi->write_feedback_v1_voice_runtime_sessions_session_id_feedback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **voice_runtime_feedback_request** | [**VoiceRuntimeFeedbackRequest**](VoiceRuntimeFeedbackRequest.md)|  | 

### Return type

[**EnvelopeVoiceRuntimeFeedbackResponse**](EnvelopeVoiceRuntimeFeedbackResponse.md)

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

