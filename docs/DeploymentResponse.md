# DeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deployment identifier | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Deployed agent | 
**share_id** | **str** | Public share identifier for URL construction | 
**name** | **str** | Deployment name | [optional] 
**is_active** | **bool** | Whether deployment is live | 
**allowed_user_ids** | **List[str]** | Authorized user IDs | [optional] [default to []]
**config** | **Dict[str, object]** | Deployment config | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update | 

## Example

```python
from zarnite.models.deployment_response import DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentResponse from a JSON string
deployment_response_instance = DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentResponse.to_json())

# convert the object into a dict
deployment_response_dict = deployment_response_instance.to_dict()
# create an instance of DeploymentResponse from a dict
deployment_response_from_dict = DeploymentResponse.from_dict(deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


