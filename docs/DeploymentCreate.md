# DeploymentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent to deploy | 
**org_id** | **str** | Organization scope | 
**name** | **str** | Deployment name | [optional] 
**allowed_user_ids** | **List[Optional[str]]** | User IDs allowed to access this deployment (empty &#x3D; public) | [optional] [default to []]
**config** | **Dict[str, object]** | Custom deployment configuration | [optional] 

## Example

```python
from zarnite.models.deployment_create import DeploymentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentCreate from a JSON string
deployment_create_instance = DeploymentCreate.from_json(json)
# print the JSON string representation of the object
print(DeploymentCreate.to_json())

# convert the object into a dict
deployment_create_dict = deployment_create_instance.to_dict()
# create an instance of DeploymentCreate from a dict
deployment_create_from_dict = DeploymentCreate.from_dict(deployment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


