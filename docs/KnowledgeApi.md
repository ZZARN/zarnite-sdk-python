# zarnite.KnowledgeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent_document_v1_agents_agent_id_documents_document_id_delete**](KnowledgeApi.md#delete_agent_document_v1_agents_agent_id_documents_document_id_delete) | **DELETE** /v1/agents/{agent_id}/documents/{document_id} | Delete Agent Document
[**delete_org_document_v1_knowledge_documents_document_id_delete**](KnowledgeApi.md#delete_org_document_v1_knowledge_documents_document_id_delete) | **DELETE** /v1/knowledge/documents/{document_id} | Delete Org Document
[**list_agent_documents_v1_agents_agent_id_documents_get**](KnowledgeApi.md#list_agent_documents_v1_agents_agent_id_documents_get) | **GET** /v1/agents/{agent_id}/documents | List Agent Documents
[**list_org_documents_v1_knowledge_documents_get**](KnowledgeApi.md#list_org_documents_v1_knowledge_documents_get) | **GET** /v1/knowledge/documents | List Org Documents
[**upload_agent_document_v1_agents_agent_id_documents_post**](KnowledgeApi.md#upload_agent_document_v1_agents_agent_id_documents_post) | **POST** /v1/agents/{agent_id}/documents | Upload Agent Document
[**upload_org_document_v1_knowledge_documents_post**](KnowledgeApi.md#upload_org_document_v1_knowledge_documents_post) | **POST** /v1/knowledge/documents | Upload Org Document


# **delete_agent_document_v1_agents_agent_id_documents_document_id_delete**
> EnvelopeKnowledgeDeleteResponse delete_agent_document_v1_agents_agent_id_documents_document_id_delete(agent_id, document_id, org_id)

Delete Agent Document

Delete a knowledge document from an agent's KB by document_id.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_knowledge_delete_response import EnvelopeKnowledgeDeleteResponse
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
    api_instance = zarnite.KnowledgeApi(api_client)
    agent_id = 'agent_id_example' # str | 
    document_id = 'document_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Delete Agent Document
        api_response = api_instance.delete_agent_document_v1_agents_agent_id_documents_document_id_delete(agent_id, document_id, org_id)
        print("The response of KnowledgeApi->delete_agent_document_v1_agents_agent_id_documents_document_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_agent_document_v1_agents_agent_id_documents_document_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **document_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeKnowledgeDeleteResponse**](EnvelopeKnowledgeDeleteResponse.md)

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

# **delete_org_document_v1_knowledge_documents_document_id_delete**
> EnvelopeKnowledgeDeleteResponse delete_org_document_v1_knowledge_documents_document_id_delete(document_id, org_id)

Delete Org Document

Delete a knowledge document from the org-wide KB by document_id.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_knowledge_delete_response import EnvelopeKnowledgeDeleteResponse
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
    api_instance = zarnite.KnowledgeApi(api_client)
    document_id = 'document_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Delete Org Document
        api_response = api_instance.delete_org_document_v1_knowledge_documents_document_id_delete(document_id, org_id)
        print("The response of KnowledgeApi->delete_org_document_v1_knowledge_documents_document_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_org_document_v1_knowledge_documents_document_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeKnowledgeDeleteResponse**](EnvelopeKnowledgeDeleteResponse.md)

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

# **list_agent_documents_v1_agents_agent_id_documents_get**
> EnvelopeListKnowledgeDocument list_agent_documents_v1_agents_agent_id_documents_get(agent_id, org_id)

List Agent Documents

List knowledge documents uploaded to an agent's KB.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_knowledge_document import EnvelopeListKnowledgeDocument
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
    api_instance = zarnite.KnowledgeApi(api_client)
    agent_id = 'agent_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # List Agent Documents
        api_response = api_instance.list_agent_documents_v1_agents_agent_id_documents_get(agent_id, org_id)
        print("The response of KnowledgeApi->list_agent_documents_v1_agents_agent_id_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->list_agent_documents_v1_agents_agent_id_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeListKnowledgeDocument**](EnvelopeListKnowledgeDocument.md)

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

# **list_org_documents_v1_knowledge_documents_get**
> EnvelopeListKnowledgeDocument list_org_documents_v1_knowledge_documents_get(org_id)

List Org Documents

List knowledge documents uploaded to the org-wide KB.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_knowledge_document import EnvelopeListKnowledgeDocument
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
    api_instance = zarnite.KnowledgeApi(api_client)
    org_id = 'org_id_example' # str | Organization scope

    try:
        # List Org Documents
        api_response = api_instance.list_org_documents_v1_knowledge_documents_get(org_id)
        print("The response of KnowledgeApi->list_org_documents_v1_knowledge_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->list_org_documents_v1_knowledge_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeListKnowledgeDocument**](EnvelopeListKnowledgeDocument.md)

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

# **upload_agent_document_v1_agents_agent_id_documents_post**
> EnvelopeKnowledgeUploadResponse upload_agent_document_v1_agents_agent_id_documents_post(agent_id, file, org_id, user_id=user_id)

Upload Agent Document

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_knowledge_upload_response import EnvelopeKnowledgeUploadResponse
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
    api_instance = zarnite.KnowledgeApi(api_client)
    agent_id = 'agent_id_example' # str | 
    file = None # bytes | 
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Upload Agent Document
        api_response = api_instance.upload_agent_document_v1_agents_agent_id_documents_post(agent_id, file, org_id, user_id=user_id)
        print("The response of KnowledgeApi->upload_agent_document_v1_agents_agent_id_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->upload_agent_document_v1_agents_agent_id_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **file** | **bytes**|  | 
 **org_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**EnvelopeKnowledgeUploadResponse**](EnvelopeKnowledgeUploadResponse.md)

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

# **upload_org_document_v1_knowledge_documents_post**
> EnvelopeKnowledgeUploadResponse upload_org_document_v1_knowledge_documents_post(file, org_id, user_id=user_id)

Upload Org Document

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_knowledge_upload_response import EnvelopeKnowledgeUploadResponse
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
    api_instance = zarnite.KnowledgeApi(api_client)
    file = None # bytes | 
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Upload Org Document
        api_response = api_instance.upload_org_document_v1_knowledge_documents_post(file, org_id, user_id=user_id)
        print("The response of KnowledgeApi->upload_org_document_v1_knowledge_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->upload_org_document_v1_knowledge_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 
 **org_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**EnvelopeKnowledgeUploadResponse**](EnvelopeKnowledgeUploadResponse.md)

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

