# zarnite.PlaygroundApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap_session_v1_playground_sessions_post**](PlaygroundApi.md#bootstrap_session_v1_playground_sessions_post) | **POST** /v1/playground/sessions | Bootstrap Session
[**end_session_v1_playground_sessions_session_id_end_post**](PlaygroundApi.md#end_session_v1_playground_sessions_session_id_end_post) | **POST** /v1/playground/sessions/{session_id}/end | End Session
[**mark_activity_v1_playground_sessions_session_id_activity_post**](PlaygroundApi.md#mark_activity_v1_playground_sessions_session_id_activity_post) | **POST** /v1/playground/sessions/{session_id}/activity | Mark Activity
[**recent_transcripts_v1_playground_transcripts_recent_get**](PlaygroundApi.md#recent_transcripts_v1_playground_transcripts_recent_get) | **GET** /v1/playground/transcripts/recent | Recent Transcripts
[**session_diagnostics_v1_playground_sessions_session_id_diagnostics_get**](PlaygroundApi.md#session_diagnostics_v1_playground_sessions_session_id_diagnostics_get) | **GET** /v1/playground/sessions/{session_id}/diagnostics | Session Diagnostics
[**session_metrics_v1_playground_sessions_session_id_metrics_get**](PlaygroundApi.md#session_metrics_v1_playground_sessions_session_id_metrics_get) | **GET** /v1/playground/sessions/{session_id}/metrics | Session Metrics
[**session_transcript_v1_playground_sessions_session_id_transcript_get**](PlaygroundApi.md#session_transcript_v1_playground_sessions_session_id_transcript_get) | **GET** /v1/playground/sessions/{session_id}/transcript | Session Transcript
[**supported_voices_v1_playground_voices_get**](PlaygroundApi.md#supported_voices_v1_playground_voices_get) | **GET** /v1/playground/voices | Supported Voices
[**voice_lookup_v1_playground_voices_lookup_get**](PlaygroundApi.md#voice_lookup_v1_playground_voices_lookup_get) | **GET** /v1/playground/voices/lookup | Voice Lookup


# **bootstrap_session_v1_playground_sessions_post**
> EnvelopePlaygroundSessionResponse bootstrap_session_v1_playground_sessions_post(playground_session_request)

Bootstrap Session

Bootstrap a Playground voice session.

Creates a DB record, mints a LiveKit token, and returns connection details.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_session_response import EnvelopePlaygroundSessionResponse
from zarnite.models.playground_session_request import PlaygroundSessionRequest
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
    api_instance = zarnite.PlaygroundApi(api_client)
    playground_session_request = zarnite.PlaygroundSessionRequest() # PlaygroundSessionRequest | 

    try:
        # Bootstrap Session
        api_response = api_instance.bootstrap_session_v1_playground_sessions_post(playground_session_request)
        print("The response of PlaygroundApi->bootstrap_session_v1_playground_sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->bootstrap_session_v1_playground_sessions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playground_session_request** | [**PlaygroundSessionRequest**](PlaygroundSessionRequest.md)|  | 

### Return type

[**EnvelopePlaygroundSessionResponse**](EnvelopePlaygroundSessionResponse.md)

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

# **end_session_v1_playground_sessions_session_id_end_post**
> EnvelopePlaygroundEndResponse end_session_v1_playground_sessions_session_id_end_post(session_id, playground_end_request)

End Session

End a Playground voice session.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_end_response import EnvelopePlaygroundEndResponse
from zarnite.models.playground_end_request import PlaygroundEndRequest
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
    api_instance = zarnite.PlaygroundApi(api_client)
    session_id = 'session_id_example' # str | 
    playground_end_request = zarnite.PlaygroundEndRequest() # PlaygroundEndRequest | 

    try:
        # End Session
        api_response = api_instance.end_session_v1_playground_sessions_session_id_end_post(session_id, playground_end_request)
        print("The response of PlaygroundApi->end_session_v1_playground_sessions_session_id_end_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->end_session_v1_playground_sessions_session_id_end_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **playground_end_request** | [**PlaygroundEndRequest**](PlaygroundEndRequest.md)|  | 

### Return type

[**EnvelopePlaygroundEndResponse**](EnvelopePlaygroundEndResponse.md)

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

# **mark_activity_v1_playground_sessions_session_id_activity_post**
> EnvelopePlaygroundActivityResponse mark_activity_v1_playground_sessions_session_id_activity_post(session_id)

Mark Activity

Heartbeat endpoint used by the client to keep a session alive.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_activity_response import EnvelopePlaygroundActivityResponse
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
    api_instance = zarnite.PlaygroundApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Mark Activity
        api_response = api_instance.mark_activity_v1_playground_sessions_session_id_activity_post(session_id)
        print("The response of PlaygroundApi->mark_activity_v1_playground_sessions_session_id_activity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->mark_activity_v1_playground_sessions_session_id_activity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**EnvelopePlaygroundActivityResponse**](EnvelopePlaygroundActivityResponse.md)

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

# **recent_transcripts_v1_playground_transcripts_recent_get**
> EnvelopeListPlaygroundSessionTranscriptResponse recent_transcripts_v1_playground_transcripts_recent_get(org_id, agent_id, user_id, limit=limit)

Recent Transcripts

Return the last few LiveKit session transcripts for one user and agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_playground_session_transcript_response import EnvelopeListPlaygroundSessionTranscriptResponse
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
    api_instance = zarnite.PlaygroundApi(api_client)
    org_id = 'org_id_example' # str | 
    agent_id = 'agent_id_example' # str | 
    user_id = 'user_id_example' # str | 
    limit = 5 # int |  (optional) (default to 5)

    try:
        # Recent Transcripts
        api_response = api_instance.recent_transcripts_v1_playground_transcripts_recent_get(org_id, agent_id, user_id, limit=limit)
        print("The response of PlaygroundApi->recent_transcripts_v1_playground_transcripts_recent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->recent_transcripts_v1_playground_transcripts_recent_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **agent_id** | **str**|  | 
 **user_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 5]

### Return type

[**EnvelopeListPlaygroundSessionTranscriptResponse**](EnvelopeListPlaygroundSessionTranscriptResponse.md)

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

# **session_diagnostics_v1_playground_sessions_session_id_diagnostics_get**
> EnvelopePlaygroundSessionDiagnosticsResponse session_diagnostics_v1_playground_sessions_session_id_diagnostics_get(session_id)

Session Diagnostics

Get frontend-friendly Playground diagnostics for latency, config, quota, and events.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_session_diagnostics_response import EnvelopePlaygroundSessionDiagnosticsResponse
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
    api_instance = zarnite.PlaygroundApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Session Diagnostics
        api_response = api_instance.session_diagnostics_v1_playground_sessions_session_id_diagnostics_get(session_id)
        print("The response of PlaygroundApi->session_diagnostics_v1_playground_sessions_session_id_diagnostics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->session_diagnostics_v1_playground_sessions_session_id_diagnostics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**EnvelopePlaygroundSessionDiagnosticsResponse**](EnvelopePlaygroundSessionDiagnosticsResponse.md)

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

# **session_metrics_v1_playground_sessions_session_id_metrics_get**
> EnvelopePlaygroundMetricsResponse session_metrics_v1_playground_sessions_session_id_metrics_get(session_id)

Session Metrics

Get debug telemetry for a Playground session.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_metrics_response import EnvelopePlaygroundMetricsResponse
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
    api_instance = zarnite.PlaygroundApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Session Metrics
        api_response = api_instance.session_metrics_v1_playground_sessions_session_id_metrics_get(session_id)
        print("The response of PlaygroundApi->session_metrics_v1_playground_sessions_session_id_metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->session_metrics_v1_playground_sessions_session_id_metrics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**EnvelopePlaygroundMetricsResponse**](EnvelopePlaygroundMetricsResponse.md)

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

# **session_transcript_v1_playground_sessions_session_id_transcript_get**
> EnvelopePlaygroundSessionTranscriptResponse session_transcript_v1_playground_sessions_session_id_transcript_get(session_id)

Session Transcript

Return the full ordered transcript for one LiveKit voice session.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_session_transcript_response import EnvelopePlaygroundSessionTranscriptResponse
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
    api_instance = zarnite.PlaygroundApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Session Transcript
        api_response = api_instance.session_transcript_v1_playground_sessions_session_id_transcript_get(session_id)
        print("The response of PlaygroundApi->session_transcript_v1_playground_sessions_session_id_transcript_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->session_transcript_v1_playground_sessions_session_id_transcript_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**EnvelopePlaygroundSessionTranscriptResponse**](EnvelopePlaygroundSessionTranscriptResponse.md)

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

# **supported_voices_v1_playground_voices_get**
> EnvelopeListStr supported_voices_v1_playground_voices_get(org_id=org_id, user_id=user_id)

Supported Voices

Return canonical Gemini voice names accepted by Playground sessions.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_str import EnvelopeListStr
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
    api_instance = zarnite.PlaygroundApi(api_client)
    org_id = 'org_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Supported Voices
        api_response = api_instance.supported_voices_v1_playground_voices_get(org_id=org_id, user_id=user_id)
        print("The response of PlaygroundApi->supported_voices_v1_playground_voices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->supported_voices_v1_playground_voices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**EnvelopeListStr**](EnvelopeListStr.md)

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

# **voice_lookup_v1_playground_voices_lookup_get**
> EnvelopePlaygroundVoiceLookupResponse voice_lookup_v1_playground_voices_lookup_get(org_id, user_id=user_id)

Voice Lookup

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_playground_voice_lookup_response import EnvelopePlaygroundVoiceLookupResponse
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
    api_instance = zarnite.PlaygroundApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Voice Lookup
        api_response = api_instance.voice_lookup_v1_playground_voices_lookup_get(org_id, user_id=user_id)
        print("The response of PlaygroundApi->voice_lookup_v1_playground_voices_lookup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaygroundApi->voice_lookup_v1_playground_voices_lookup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**EnvelopePlaygroundVoiceLookupResponse**](EnvelopePlaygroundVoiceLookupResponse.md)

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

