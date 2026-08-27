# DeploymentShareVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized** | **bool** | Whether learner is authorized | [optional] [default to True]
**learner** | **Dict[str, object]** | Verified learner context | 
**deployment** | **Dict[str, object]** | Resolved deployment context | 

## Example

```python
from zarnite.models.deployment_share_verify_response import DeploymentShareVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentShareVerifyResponse from a JSON string
deployment_share_verify_response_instance = DeploymentShareVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentShareVerifyResponse.to_json())

# convert the object into a dict
deployment_share_verify_response_dict = deployment_share_verify_response_instance.to_dict()
# create an instance of DeploymentShareVerifyResponse from a dict
deployment_share_verify_response_from_dict = DeploymentShareVerifyResponse.from_dict(deployment_share_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


