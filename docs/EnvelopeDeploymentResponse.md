# EnvelopeDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeploymentResponse**](DeploymentResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_deployment_response import EnvelopeDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeDeploymentResponse from a JSON string
envelope_deployment_response_instance = EnvelopeDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeDeploymentResponse.to_json())

# convert the object into a dict
envelope_deployment_response_dict = envelope_deployment_response_instance.to_dict()
# create an instance of EnvelopeDeploymentResponse from a dict
envelope_deployment_response_from_dict = EnvelopeDeploymentResponse.from_dict(envelope_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


