# DeploymentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name | [optional] 
**is_active** | **bool** | Activate or deactivate | [optional] 
**allowed_user_ids** | **List[str]** | Updated access list | [optional] 
**config** | **Dict[str, object]** | Updated config | [optional] 

## Example

```python
from zarnite.models.deployment_update import DeploymentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentUpdate from a JSON string
deployment_update_instance = DeploymentUpdate.from_json(json)
# print the JSON string representation of the object
print(DeploymentUpdate.to_json())

# convert the object into a dict
deployment_update_dict = deployment_update_instance.to_dict()
# create an instance of DeploymentUpdate from a dict
deployment_update_from_dict = DeploymentUpdate.from_dict(deployment_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


