# DeploymentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deleted deployment identifier | 
**deleted** | **bool** | Deletion result | [optional] [default to True]

## Example

```python
from zarnite.models.deployment_delete_response import DeploymentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentDeleteResponse from a JSON string
deployment_delete_response_instance = DeploymentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentDeleteResponse.to_json())

# convert the object into a dict
deployment_delete_response_dict = deployment_delete_response_instance.to_dict()
# create an instance of DeploymentDeleteResponse from a dict
deployment_delete_response_from_dict = DeploymentDeleteResponse.from_dict(deployment_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


