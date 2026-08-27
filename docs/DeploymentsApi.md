# zarnite.DeploymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment_v1_deployments_post**](DeploymentsApi.md#create_deployment_v1_deployments_post) | **POST** /v1/deployments/ | Create Deployment
[**delete_deployment_v1_deployments_deploy_id_delete**](DeploymentsApi.md#delete_deployment_v1_deployments_deploy_id_delete) | **DELETE** /v1/deployments/{deploy_id} | Delete Deployment
[**list_deployments_v1_deployments_get**](DeploymentsApi.md#list_deployments_v1_deployments_get) | **GET** /v1/deployments/ | List Deployments
[**resolve_share_v1_deployments_share_share_id_get**](DeploymentsApi.md#resolve_share_v1_deployments_share_share_id_get) | **GET** /v1/deployments/share/{share_id} | Resolve Share
[**update_deployment_v1_deployments_deploy_id_put**](DeploymentsApi.md#update_deployment_v1_deployments_deploy_id_put) | **PUT** /v1/deployments/{deploy_id} | Update Deployment
[**verify_share_access_v1_deployments_share_share_id_verify_post**](DeploymentsApi.md#verify_share_access_v1_deployments_share_share_id_verify_post) | **POST** /v1/deployments/share/{share_id}/verify | Verify Share Access


# **create_deployment_v1_deployments_post**
> EnvelopeDeploymentResponse create_deployment_v1_deployments_post(deployment_create)

Create Deployment

Create a new deployment with a unique share link.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.deployment_create import DeploymentCreate
from zarnite.models.envelope_deployment_response import EnvelopeDeploymentResponse
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
    api_instance = zarnite.DeploymentsApi(api_client)
    deployment_create = zarnite.DeploymentCreate() # DeploymentCreate | 

    try:
        # Create Deployment
        api_response = api_instance.create_deployment_v1_deployments_post(deployment_create)
        print("The response of DeploymentsApi->create_deployment_v1_deployments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->create_deployment_v1_deployments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_create** | [**DeploymentCreate**](DeploymentCreate.md)|  | 

### Return type

[**EnvelopeDeploymentResponse**](EnvelopeDeploymentResponse.md)

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

# **delete_deployment_v1_deployments_deploy_id_delete**
> EnvelopeDeploymentDeleteResponse delete_deployment_v1_deployments_deploy_id_delete(deploy_id, org_id)

Delete Deployment

Delete a deployment.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_deployment_delete_response import EnvelopeDeploymentDeleteResponse
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
    api_instance = zarnite.DeploymentsApi(api_client)
    deploy_id = 'deploy_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope

    try:
        # Delete Deployment
        api_response = api_instance.delete_deployment_v1_deployments_deploy_id_delete(deploy_id, org_id)
        print("The response of DeploymentsApi->delete_deployment_v1_deployments_deploy_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->delete_deployment_v1_deployments_deploy_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 

### Return type

[**EnvelopeDeploymentDeleteResponse**](EnvelopeDeploymentDeleteResponse.md)

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

# **list_deployments_v1_deployments_get**
> EnvelopeListDeploymentResponse list_deployments_v1_deployments_get(org_id, agent_id=agent_id)

List Deployments

List deployments for an organization, optionally filtered by agent.

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.envelope_list_deployment_response import EnvelopeListDeploymentResponse
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
    api_instance = zarnite.DeploymentsApi(api_client)
    org_id = 'org_id_example' # str | Organization scope
    agent_id = 'agent_id_example' # str | Filter by agent (optional)

    try:
        # List Deployments
        api_response = api_instance.list_deployments_v1_deployments_get(org_id, agent_id=agent_id)
        print("The response of DeploymentsApi->list_deployments_v1_deployments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->list_deployments_v1_deployments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization scope | 
 **agent_id** | **str**| Filter by agent | [optional] 

### Return type

[**EnvelopeListDeploymentResponse**](EnvelopeListDeploymentResponse.md)

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

# **resolve_share_v1_deployments_share_share_id_get**
> EnvelopeDeploymentResponse resolve_share_v1_deployments_share_share_id_get(share_id)

Resolve Share

Public endpoint: resolve a share link to its deployment config. No auth required.

### Example


```python
import zarnite
from zarnite.models.envelope_deployment_response import EnvelopeDeploymentResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.DeploymentsApi(api_client)
    share_id = 'share_id_example' # str | 

    try:
        # Resolve Share
        api_response = api_instance.resolve_share_v1_deployments_share_share_id_get(share_id)
        print("The response of DeploymentsApi->resolve_share_v1_deployments_share_share_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->resolve_share_v1_deployments_share_share_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_id** | **str**|  | 

### Return type

[**EnvelopeDeploymentResponse**](EnvelopeDeploymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment_v1_deployments_deploy_id_put**
> EnvelopeDeploymentResponse update_deployment_v1_deployments_deploy_id_put(deploy_id, org_id, deployment_update)

Update Deployment

Update deployment settings (name, active status, access list, config).

### Example

* Bearer Authentication (HTTPBearer):

```python
import zarnite
from zarnite.models.deployment_update import DeploymentUpdate
from zarnite.models.envelope_deployment_response import EnvelopeDeploymentResponse
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
    api_instance = zarnite.DeploymentsApi(api_client)
    deploy_id = 'deploy_id_example' # str | 
    org_id = 'org_id_example' # str | Organization scope
    deployment_update = zarnite.DeploymentUpdate() # DeploymentUpdate | 

    try:
        # Update Deployment
        api_response = api_instance.update_deployment_v1_deployments_deploy_id_put(deploy_id, org_id, deployment_update)
        print("The response of DeploymentsApi->update_deployment_v1_deployments_deploy_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->update_deployment_v1_deployments_deploy_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_id** | **str**|  | 
 **org_id** | **str**| Organization scope | 
 **deployment_update** | [**DeploymentUpdate**](DeploymentUpdate.md)|  | 

### Return type

[**EnvelopeDeploymentResponse**](EnvelopeDeploymentResponse.md)

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

# **verify_share_access_v1_deployments_share_share_id_verify_post**
> EnvelopeDeploymentShareVerifyResponse verify_share_access_v1_deployments_share_share_id_verify_post(share_id, deployment_share_verify_request)

Verify Share Access

Public endpoint: verify learner credentials for a deployment share link.

### Example


```python
import zarnite
from zarnite.models.deployment_share_verify_request import DeploymentShareVerifyRequest
from zarnite.models.envelope_deployment_share_verify_response import EnvelopeDeploymentShareVerifyResponse
from zarnite.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = zarnite.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with zarnite.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarnite.DeploymentsApi(api_client)
    share_id = 'share_id_example' # str | 
    deployment_share_verify_request = zarnite.DeploymentShareVerifyRequest() # DeploymentShareVerifyRequest | 

    try:
        # Verify Share Access
        api_response = api_instance.verify_share_access_v1_deployments_share_share_id_verify_post(share_id, deployment_share_verify_request)
        print("The response of DeploymentsApi->verify_share_access_v1_deployments_share_share_id_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->verify_share_access_v1_deployments_share_share_id_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_id** | **str**|  | 
 **deployment_share_verify_request** | [**DeploymentShareVerifyRequest**](DeploymentShareVerifyRequest.md)|  | 

### Return type

[**EnvelopeDeploymentShareVerifyResponse**](EnvelopeDeploymentShareVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

