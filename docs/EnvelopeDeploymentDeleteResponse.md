# EnvelopeDeploymentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeploymentDeleteResponse**](DeploymentDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_deployment_delete_response import EnvelopeDeploymentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeDeploymentDeleteResponse from a JSON string
envelope_deployment_delete_response_instance = EnvelopeDeploymentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeDeploymentDeleteResponse.to_json())

# convert the object into a dict
envelope_deployment_delete_response_dict = envelope_deployment_delete_response_instance.to_dict()
# create an instance of EnvelopeDeploymentDeleteResponse from a dict
envelope_deployment_delete_response_from_dict = EnvelopeDeploymentDeleteResponse.from_dict(envelope_deployment_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


